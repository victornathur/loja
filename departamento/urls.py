from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('camisa/', views.camisa_list),
    path('camisa/<int:camisa_id>/', views.camisa_show),
   
]
