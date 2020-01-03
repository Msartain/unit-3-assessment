from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.WishCreate.as_view(), name='create'),
    path('<int:pk>/delete/', views.WishDelete.as_view(), name='delete'),

]
