from django.db import models

class User(models.Model):
    userId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=200)
    personal_no = models.CharField(max_length=10)
    home_no = models.CharField(max_length=1000)
    username = models.CharField(max_length=1000)
    password = models.CharField(max_length=1000)

class Hobby(models.Model):
    hobbyId = models.AutoField(primary_key=True)
    hobbyTitle = models.CharField(max_length=500)
    hobbyBody = models.TextField(max_length=500)
    userId = models.ForeignKey(User.UserId, blank=True, null=True)

    

