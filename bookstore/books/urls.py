from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('delete/<int:id>', views.destroy,name='destroy'),
    path('show/<int:id>', views.show,name='show'), 
    path('edit/<int:id>', views.edit,name='edit'), \
    # path('api/', views.books_details), 
    path('api/', views.books_list),
    path('api/<int:pk>/', views.books_details),
]

