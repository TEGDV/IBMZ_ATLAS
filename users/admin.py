from django.contrib import admin
from users.models import EmployeeProfile
# Register your models here, if you want to see them into the Django admin site insted of use 
# Your database console.
@admin.register(EmployeeProfile)
class EmployeeProfileAdmin(admin.ModelAdmin):
    #Profile admin
    pass