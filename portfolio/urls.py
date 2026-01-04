from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.admin),
    path('', include('portfolio.urls')), # connects app to main site
]