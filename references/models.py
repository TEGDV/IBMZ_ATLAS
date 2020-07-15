from django.db import models

# Create your models here.
class Refcodes(models.Model):
    # DB references codes table model

    ref_code = models.TextField(unique=True, max_length=30)
    system_number = models.TextField(max_length=30,blank=True)
    operation_number = models.TextField(max_length=30)
    operation_name = models.TextField(max_length=30)
    hmdescription = models.TextField(max_length=300, blank=True)
    fix_action = models.TextField(max_length=300,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.TextField(max_length=30)