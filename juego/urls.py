from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.iniciar_juego, name='iniciar'),  # Ruta inicial
    path('juego/', views.juego, name='juego'),    # Ruta principal del juego
    path('reiniciar/', views.reiniciar, name='reiniciar'),  # Ruta para reiniciar el juego
]
