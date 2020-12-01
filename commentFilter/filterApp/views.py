from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
from django.urls import reverse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Photo

class PhotoList(ListView):
    model = Photo
    template_name_suffix = '_list'

class PhotoCreate(CreateView):
    model = Photo
    fields = ['text', 'image']
    template_name_suffix = '_create'
    success_url = '/'

class PhotoUpdate(UpdateView):
    model = Photo
    fields = ['text', 'image']
    template_name_suffix = '_update'
    success_url = '/'

class PhotoDelete(DeleteView):
    medel = Photo
    template_name_suffix = '_delete'
    success_url = '/'

class PhotoDetail(DeleteView):
    model = Photo
    template_name_suffix = '_detail'



# Create your views here.

def index(request):
    return render(request, 'filterApp/index.html')

def login(request):
    email = request.POST['email']
    pwd = request.POST['password']
    print(">>>>>>>>>>>>>>>>>>>>>>>>> ", email)
    print(">>>>>>>>>>>>>>>>>>>>>>>>> ", pwd)
    try:
        user = User.objects.get(user_email=email, user_pwd=pwd)
        print(">>>>>>>>>>> login success", user.user_name)
    except:
        return redirect('index')

    context = {}
    if user is not None :
        request.session['user_name'] = user.user_name
        request.session['user_email'] = user.user_email
        context['name']  = request.session['user_name']
        context['email'] = request.session['user_email']
        return render(request, 'filterApp/../layout/profile.html', context)
    # else:
    #     return redirect('login')
    return render(request, 'filterApp/index.html')



def register(request) :
    if request.method == 'POST':
        email = request.POST['email']
        pwd = request.POST['password']
        name = request.POST['name']

        register = User(user_email=email, user_pwd=pwd, user_name=name)
        register.save()
        print('>>>>>>>>>>>>>>>>>>>>', register.user_name)
    return redirect('index')

def profile(request):
    return render(request, 'filterApp/../layout/profile.html')

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

def createText(request):
    return HttpResponse('createText를 할거야!')
