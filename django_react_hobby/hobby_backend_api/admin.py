from django.contrib import admin
from .models import User, Hobby

models_list = [User, Hobby]
admin.site.register(models_list)