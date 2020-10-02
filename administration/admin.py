from django.contrib import admin
from .models import ClientDetails, ProjectDetails, MiscellaneousDetails

admin.site.register(ClientDetails)
admin.site.register(ProjectDetails)
admin.site.register(MiscellaneousDetails)