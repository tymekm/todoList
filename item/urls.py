from django.urls import path
from . import views

app_name = 'item'
urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:id>/', views.details, name='details'),
    path('newItem/', views.newItem, name='newItem'),
    path('newItem/<int:id>/', views.newItem, name='newItem'),
    path('editItem/<int:id>/', views.editItem, name='editItem'),
    path('completeItem/<int:id>/', views.completeItem, name='completeItem'),
    path('deleteItem/<int:id>/', views.deleteItem, name='deleteItem')
]
