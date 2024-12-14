from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('' ,views.indexview.as_view(), name='core_index'),
    path('create/', views.createview.as_view(), name='core_create'),
    path('delete/<int:pk>', views.deleteview.as_view(), name='core_delete'),
    # Practice
    path('new_create/', views.newcreate.as_view(), name='newcreate'),
    path('new_index/', views.newindex.as_view(), name='newindex'),
    path('new_delete/<int:pk>', views.newdelete.as_view(), name='newdelete'),
    path('update/<int:pk>/', views.newupdate.as_view(), name='newupdate'),
    # Alenere
    path('alenere_index/', views.alenereindex.as_view(), name='alenereindex'),
    path('alenere_create/', views.alenerecreate.as_view(), name='alenerecreate'),
    path('alenere_delete/<int:pk>', views.aleneredelete.as_view(), name='aleneredelete'),
    path('alenere_update/<int:pk>', views.alenereupdate.as_view(), name='alenereupdate'),
    path('alenere_detail/<int:pk>', views.aleneredetail.as_view(), name='aleneredetail')
    # Name = reverse, reverse lazy, url
]
