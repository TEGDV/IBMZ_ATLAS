from django.contrib import admin
from django.urls import path
from posts import views as post_views
from references import views as ref_views
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/blog/', post_views.list_post, name='blog'),
    path('account/references/', ref_views.references_db, name='reftable'),
    path('account/login/',users_views.login_view, name='login'),
    path('account/logout/',users_views.logout_view, name='logout'),
    path('account/register/',users_views.register, name='register'),
    path('account/home',users_views.home, name='home'),
    path('account/profile',users_views.profile, name='profile'),
]
