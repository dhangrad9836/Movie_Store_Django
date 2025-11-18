from django.urls import path    # path is used to define URL paterns
from . import views # this is to import the views file

# urlpatterns to define our list of paths
urlpatterns = [
    path('', views.index, name='home.index'),
    path('about', views.about, name='home.about'),
]