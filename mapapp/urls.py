from django.urls import path
from . import views

urlpatterns = [
    path('', views.map_view, name='map'),          # Homepage with all user markers
    path('add/', views.user_create, name='user_create'),  # Page with the user form
]
