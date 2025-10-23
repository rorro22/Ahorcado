"""
URL configuration for ahorcado project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from juego import views

urlpatterns = [
    path('', views.iniciar_juego, name='home'),  # ← Esta es la nueva línea
    path('index/', views.iniciar_juego, name='iniciar'),
    path('juego/', views.juego, name='juego'),
    path('reiniciar/', views.reiniciar_juego, name='reiniciar'),
    path('admin/', admin.site.urls),
]
