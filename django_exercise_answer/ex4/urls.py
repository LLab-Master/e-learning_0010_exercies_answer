from django.urls import path
from . import views

app_name = "ex4"

urlpatterns = [
    path('', views.input1, name='input1'),
]
