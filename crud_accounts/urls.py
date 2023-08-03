from django.urls import path 
from .views import *

urlpatterns = [
    path('proj/',ProjectAPI.as_view()),
    path('proj/<int:pk>/',ProjectDetailsAPI.as_view()),
]

