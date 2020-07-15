from django.contrib import admin
from django.urls import path
from posts import views as post_views
from references import views as ref_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', post_views.list_post),
    path('references/', ref_views.references_db),
]
