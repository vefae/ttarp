from django.urls import path
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    path('', views.home),
    path('login/', login, {'template_name': 'home/login.html'}),
    path('logout/', logout, {'template_name': 'home/logout.html'}),
    path('inventory/', logout, {'template_name': 'inventory/inventory.html'}),

]
