from django.urls import path
from . import views

app_name = "ex3"

urlpatterns = [
    path('input1/', views.input1, name='input1'),
    path('show1/', views.show1, name='show1'),
    path('input2/<str:param1>', views.input2, name='input2'),
]
