from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexed, name='index'),
    path('info_dispositivo/', views.get_agent, name='info_dispositivo'),
    path('user-agent/info', views.info_agent, name='info_user_agent'),
]