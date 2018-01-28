from django.urls import path
from . import views


urlpatterns = [

    path('', views.inventory),
    path('create/', views.save_inv)
]
