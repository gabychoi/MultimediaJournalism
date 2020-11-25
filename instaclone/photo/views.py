from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Photo

class PhotoList(ListView) :
    model = Photo
    template_name_suffix = 'list'

class PhotoCreate(CreateView) :
    model = Photo
    fields = ['text', 'image']
    template_name_suffix = '_create'
    success_url = '/'

class PhotoUpdate(UpdateView) :
    model = Photo
    fields = ['text', 'image']
    template_name_suffix = '_update'
    success_url = '/'

class PhotoDelete(DeleteView) :
    model = Photo
    template_name_suffix = '_delete'
    success_url = '/'

class PhotoDetail(DeleteView) :
    model = Photo
    template_name_suffix = '_detail'


