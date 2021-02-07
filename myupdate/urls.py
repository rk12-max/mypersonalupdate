from django.urls import path
from .  import views

urlpatterns = [
    path('', views.Home,name='Home'),
    path('delete/<int:id>',views.Delete,name='Delete'),
    path('complete/<int:id>',views.Complete,name='Complete'),
    path('uncomplete/<int:id>',views.Uncomplete,name='Uncomplete'),
]
