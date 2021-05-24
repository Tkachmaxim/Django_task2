"""stepik_tours URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import tours.views as tour

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tour.main_view, name='index'),
    path('departure/<str:departure>/', tour.departure_view, name='departure'),
    path('tour/<int:pk>/', tour.tour_view, name='tour')
]

handler400 = tour.c_handler400
handler500 = tour.c_handler500
