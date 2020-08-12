from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import EmployeeProfile, HomeAd
from django.contrib.auth.models import User
# Register your models here, if you want to see them into the Django admin site insted of use 
# Your database console.

@admin.register(HomeAd)
class HomeAdadmin(admin.ModelAdmin):
    pass

@admin.register(EmployeeProfile)
class EmployeeProfileAdmin(admin.ModelAdmin):
    #Profile admin
    list_display = ('pk','user','phone_number', 'website', 'picture','resume')
    #list editable to make editable cells into your admin
    #Search field to create filters into the admin search text bar 
    # list filter makes a new quck filter box 
    # Field sets to to accommodate the way the fields look
    # Readonly fields to block the able of edit some field
class EmployeeProfileInLine(admin.StackedInline):
    # Profile in line admin for unregister users.

    model = EmployeeProfile
    can_delete = False
    verbose_name_plural = 'employeeprofiles'

class UserAdmin(BaseUserAdmin):
    # add profile admin to base user admin
    inlines = (EmployeeProfileInLine,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )

admin.site.unregister(User)
admin.site.register(User,UserAdmin)