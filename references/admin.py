from django.contrib import admin
from references.models import Refcode
# Register your models here.
@admin.register(Refcode)
class RefCodeAdmin(admin.ModelAdmin):
    #Profile admin
    pass