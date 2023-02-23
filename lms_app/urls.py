from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('books', views.books, name= 'books'),
    path('<int:id>update', views.update, name= 'update'),
    path('<int:id>delete', views.delete, name= 'delete'),
]
