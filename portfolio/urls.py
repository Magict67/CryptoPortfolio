from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio_list, name='portfolio_list'),
    path('add/', views.add_coin, name='add_coin'), # new addy line!
]