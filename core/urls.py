
from django.contrib import admin
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('logar', views.logar, name='logar'),
    path('sair', views.sair, name='sair'),
    path('login_views', views.login_views, name='login_views'),
    path('sistema/<int:pk>/', views.home, name='sistema'),
    
    path('pessoa/<int:pk>/', views.lista_pessoa, name='lista_pessoa'),
    path('pessoa_novo/<int:pk>/', views.pessoa_novo, name='pessoa_novo'),
    re_path(r'^pessoa_update/(?P<id>\d+)/$', views.pessoa_update, name='pessoa_update'),
    re_path(r'^pessoa_delete/(?P<id>\d+)/$', views.pessoa_delete, name='pessoa_delete'),



    path('listaparametro_hora/<int:pk>/', views.listaparametro_hora, name='listaparametro_hora'),
    path('parametrohora_novo/<int:pk>/', views.parametrohora_novo, name='parametrohora_novo'),
    re_path(r'^parametrohora_update/(?P<id>\d+)/$', views.parametrohora_update, name='parametrohora_update'),
    re_path(r'^parametrohora_delete/(?P<id>\d+)/$', views.parametrohora_delete, name='parametrohora_delete'),



    path('listaparametro_mensal/<int:pk>/', views.listaparametro_mensal, name='listaparametro_mensal'),
    path('parametromensal_novo/<int:pk>/', views.parametromensal_novo, name='parametromensal_novo'),
    re_path(r'^parametromensal_update/(?P<id>\d+)/$', views.parametromensal_update, name='parametromensal_update'),
    re_path(r'^parametromensal_delete/(?P<id>\d+)/$', views.parametromensal_delete, name='parametromensal_delete'),






    path('veiculo/<int:pk>/', views.lista_veiculo, name='lista_veiculo'),
    path('veiculo_novo/<int:pk>/', views.veiculo_novo, name='veiculo_novo'),
    re_path(r'^veiculo_update/(?P<id>\d+)/$', views.veiculo_update, name='veiculo_update'),
    re_path(r'^veiculo_delete/(?P<id>\d+)/$', views.veiculo_delete, name='veiculo_delete'),

    path('marca/<int:pk>/', views.lista_marca, name='marca'),
    path('marca_novo/<int:pk>/', views.marca_novo, name='marca_novo'),
    re_path(r'^marca_update/(?P<id>\d+)/$', views.marca_update, name='marca_update'),
    
    path('movimento/<int:pk>/', views.lista_mov_rotativo, name='lista_mov'),
    path('rotativo_novo/<int:pk>/', views.rotativo_novo, name='rotativo_novo'),
    re_path(r'^rotativo_update/(?P<id>\d+)/$', views.rotativo_update, name='rotativo_update'),
    re_path(r'^mov_rotativo_delete/(?P<id>\d+)/$', views.mov_rotativo_delete, name='mov_rotativo_delete'),

    path('mensalista/<int:pk>/', views.lista_mensalista, name='mensalista'),
    path('mensalista_novo/<int:pk>/', views.mensalista_novo, name='mensalista_novo'),
    re_path(r'^mensalista_update/(?P<id>\d+)/$', views.mensalista_update, name='mensalista_update'),
    re_path(r'^mensalista_delete/(?P<id>\d+)/$', views.mensalista_delete, name='mensalista_delete'),


    path('mov_mensalista/<int:pk>/', views.lista_mov_mensalista, name='mov_mensalista'),
    path('mov_mensalista_novo', views.mov_mensalista_novo, name='mov_mensalista_novo'),
    re_path(r'^mov_mensalista_update/(?P<id>\d+)/$', views.mov_mensalista_update, name='mov_mensalista_update'),
    re_path(r'^mov_mensalista_delete/(?P<id>\d+)/$', views.mov_mensalista_delete, name='mov_mensalista_delete'),
]