from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/receita/<int:receita_id>/', views.api_receita),
    path('api/receitas/', views.api_receita_list),
]