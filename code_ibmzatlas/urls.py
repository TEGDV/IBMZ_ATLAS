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
    path('account/notifications',users_views.profile, name='notifications'),
    path('account/status',users_views.profile, name='status'),
    path('account/team',users_views.profile, name='team'),
    path('account/manuals',users_views.profile, name='manuals'),
    path('account/error',users_views.profile, name='error'),
   
]
