from django.urls import path
from .views import *
urlpatterns = [
    path('a1/',RegisterUser.as_view())
]
