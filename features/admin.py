from django.contrib import admin
from features.models import Refcode, Post
# Register your models here.
@admin.register(Refcode)
class RefCodeAdmin(admin.ModelAdmin):
    #Profile admin
    pass


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    #Posts admin
    pass