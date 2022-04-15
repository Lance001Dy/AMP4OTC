from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse 
#from PIL import Image

class ClientDetails(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	client = models.CharField(max_length=50)
	client_rep = models.CharField(max_length=50)
	client_rep_pos = models.CharField(max_length=50)
	client_rep_email = models.EmailField(max_length=50)
	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.client

	def get_absolute_url(self):
		return reverse('client-detail', kwargs={'pk': self.pk})

class ProjectDetails(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	client = models.ForeignKey('administration.ClientDetails', on_delete=models.CASCADE, related_name='ProjectDetails')
	site = models.CharField(max_length=50)
	section = models.CharField(max_length=50)
	location = models.CharField(max_length=50)
	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.section

	def get_absolute_url(self):
		return reverse('project-detail', kwargs={'pk1': self.pk})

class MiscellaneousDetails(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	section = models.ForeignKey('administration.ProjectDetails', on_delete=models.CASCADE, related_name='MiscellaneousDetails')
	external_env = models.CharField(max_length=50)
	corrosive_env = models.CharField(max_length=50)
	heat_env = models.CharField(max_length=50)
	major_rep = models.CharField(max_length=50)
	common_occ = models.CharField(max_length=50)
	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.external_env

	def get_absolute_url(self):
		return reverse('miscellaneous-detail', kwargs={'pk2': self.pk})
