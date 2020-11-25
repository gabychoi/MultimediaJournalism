from django.urls import path, include
from tempApp import views

urlpatterns = [
    path('',views.index),

]
