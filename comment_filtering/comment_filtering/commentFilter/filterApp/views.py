from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def index(request):
    return render(request, 'filterApp/index.html')

def profile(request):
    return render(request, 'filterApp/profile.html')

def home(request):
    return render(request, 'filterApp/home.html')

def user_detail(request):
    return render(request, 'filterApp/user_detail.html')

def edit_profile(request):
    return render(request, 'filterApp/edit_profile.html')

def profile_wall(request):
    return render(request, 'filterApp/profile_wall.html')

def view_photo(request):
    return render(request, 'filterApp/view_photo.html')

def file_manager(request):
    return render(request, 'filterApp/file_manager.html')

def friends(request):
    return render(request, 'filterApp/friends.html')
