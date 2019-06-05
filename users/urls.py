from django.urls import path

from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('change', views.update_profile, name='change')
]
