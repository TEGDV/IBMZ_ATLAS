from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Refcode(models.Model):
    # DB references codes table model

    ref_code = models.CharField(unique=True, max_length=35)
    system_number = models.CharField(max_length=30,blank=True)
    operation_number = models.CharField(max_length=30)
    operation_name = models.CharField(max_length=30)
    hmdescription = models.TextField(max_length=300, blank=True)
    fix_action = models.TextField(max_length=300,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    
class Post(models.Model):
    # DB posts model

    title = models.CharField(max_length=255,blank=False, null=False)
    topic = models.CharField(max_length=50)
    fileurl = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    profile = models.ForeignKey("users.EmployeeProfile", on_delete=models.CASCADE)

    def __str__(self):
        # return the title and username
        return f'{self.title} by @{self.user.username}'

    