from django.db import models
from django.contrib.auth.models import User
from PIL import ImageFile
# Create your models here.
class EmployeeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='users/static/pictures/', blank=True, null=True,default='users/static/pictures/default.png')
    website = models.URLField(max_length=200,blank=True)
    biography = models.TextField(max_length=200,blank=True)
    resume = models.FileField(upload_to='users/static/files/', blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
