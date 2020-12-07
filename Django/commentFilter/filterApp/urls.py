from django.urls import path
from . import views
from .views import  PhotoList, PhotoCreate, PhotoDelete, PhotoDetail, PhotoUpdate

app_name = "filterApp"


urlpatterns = [
    path('', views.index, name='index'),
    path('login/profile.html', views.profile, name='profile'),
    path('login/home.html', views.home, name='home'),
    path('login/user_detail.html', views.user_detail, name='user_detail'),
    path('login/edit_profile.html', views.edit_profile, name='edit_profile'),
    path('login/profile_wall.html', views.profile_wall, name='profile_wall'),
    path('login/view_photo.html', views.view_photo, name='view_photo'),
    path('login/file_manager.html', views.file_manager, name='file_manager'),
    path('login/friends.html', views.friends, name='friends'),
    path('login/createText/', views.createText),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),

    #가은이한테 추가해야 하는 부분(추가 완료)
    path("create/", PhotoCreate.as_view(), name='create'),
    path("delete/<int:pk>/", PhotoDelete.as_view(), name='delete'),
    path("update/<int:pk>/", PhotoUpdate.as_view(), name='update'),
    path("detail/<int:pk>/", PhotoDetail.as_view(), name="detail"),
    path("", PhotoList.as_view(), name='photo_list'),
]
