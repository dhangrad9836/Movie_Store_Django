from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='movies.index'),
    path('<int:id>/', views.show, name='movies.show'),  # we are going to pass in an integer/id to represent the each movie and pass to the show function
]