from django.contrib import admin

from .models import User, WorkerProfile
admin.site.register(User, WorkerProfile)