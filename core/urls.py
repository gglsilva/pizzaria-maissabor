from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cliente/', views.cliente_list, name='cliente_list'),
    #path('endereco/', views.endereco_detail, name='endereco_detail'),
    #path('endereco/new/', views.endereco_new, name='endereco_new'),   
]
