from django.db import models
from django.contrib.auth.models import User
from PIL import ImageFile
# Create your models here.
class EmployeeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='users/static/pictures', blank=True, null=True)


    def __str__(self):
        return self.username
