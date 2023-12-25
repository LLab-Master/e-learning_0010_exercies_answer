from django.urls import path
from . import views

app_name = "ex2"

urlpatterns = [
    path('hello1/', views.hello1, name='hello1'),
    path('hello2/', views.hello2, name='hello2'),
    path('hello3/', views.Hello3View.as_view(), name='hello3'),
    path('hello4/', views.hello4, name='hello4'),
]
