from django.contrib import admin
from django.urls import path

from features import views as features_views
from users import views as users_views

urlpatterns = [
    #Admin

    path('admin/', admin.site.urls),

    # Users views

    path('login/',users_views.login_view, name='login'),
    path('register/',users_views.register, name='register'),
    path('account/logout/',users_views.logout_view, name='logout'),
    path('account/profile',users_views.profile, name='profile'),
    path('account/notifications',users_views.profile, name='notifications'),
    path('account/settings',users_views.settings, name='settings'),
    path('account/me/update',users_views.update_profile, name='update'),

    # Features views

    path('account/blog/', features_views.list_post, name='blog'),
    path('account/home',users_views.home, name='home'),
    path('account/references/', features_views.references_db, name='reftable'),
    path('account/status',features_views.status, name='status'),
    path('account/team',features_views.teamz, name='teamz'),
    path('account/manuals',features_views.manuals, name='manuals'),
    path('account/vocabulary',features_views.vocabulary, name='vocabulary'),

    # Error views

    path('account/error',users_views.profile, name='error'),

]
