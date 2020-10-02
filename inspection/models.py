from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse 
from PIL import Image

#Test from Ubuntu PC
#Test Charl
#Test 2

class Thread(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	client = models.CharField(max_length=100)
	site = models.CharField(max_length=100)
	equipment = models.CharField(max_length=100)
	image = models.ImageField(default='default.jpg', upload_to='inspection_pics')
	date_posted = models.DateTimeField(default=timezone.now)

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)

	def __str__(self):
		return self.client

	def get_absolute_url(self):
		return reverse('thread-detail', kwargs={'pk': self.pk})

class Comment(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	thread = models.ForeignKey('inspection.thread', on_delete=models.CASCADE, related_name='comments')
	component = models.CharField(max_length=100)
	observation = models.TextField()
	assessment = models.TextField()
	action = models.TextField()
	risk = models.CharField(max_length=100)
	image = models.ImageField(default='default.jpg', upload_to='inspection_pics')
	date_posted = models.DateTimeField(default=timezone.now)
	approved_comment = models.BooleanField(default=False)

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)
	
	def approve(self):
		self.approved_comment = True
		self.save()
	def __str__(self):
		return self.component
	def get_absolute_url(self):
		return reverse('comment-detail', kwargs={'pk1': self.pk})