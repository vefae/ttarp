from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.main),
    path('inventory/', include('inventory.urls')),
]
