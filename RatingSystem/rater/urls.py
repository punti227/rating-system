
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addproduct/', views.addproduct, name='addproduct'),
    path('removeproduct/', views.removeproduct, name='removeproduct'),
]