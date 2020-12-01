from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('/filterApp/profile.html', views.profile, name='profile'),
    path('/filterApp/home.html', views.home, name='home'),
    path('/filterApp/user_detail.html', views.user_detail, name='user_detail'),
    path('/filterApp/edit_profile.html', views.edit_profile, name='edit_profile'),
    path('/filterApp/profile_wall.html', views.profile_wall, name='profile_wall'),
    path('/filterApp/view_photo.html', views.view_photo, name='view_photo'),
    path('/filterApp/file_manager.html', views.file_manager, name='file_manager'),
    path('/filterApp/friends.html', views.friends, name='friends'),
]