from django.urls import path
from . import views





#URLConf
urlpatterns = [
    path('oldHtml/', views.old_sample),
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
    path('create-room/', views.createRoom, name="createRoom"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
       
]