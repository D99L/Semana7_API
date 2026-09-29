from django.urls import path
from rest_api import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('categorias/<int:pk>/', views.detalle_categoria, name='detalle_categoria'),
    path('login/', obtain_auth_token, name='api_token_auth'),
]
