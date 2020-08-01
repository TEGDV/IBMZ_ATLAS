from django.contrib import admin
from features.models import Refcode, Post
# Register your models here.
@admin.register(Refcode)
class RefCodeAdmin(admin.ModelAdmin):
    #Profile admin
    list_display = ('pk','ref_code','system_number','created_by')


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    #Posts admin
    pass
