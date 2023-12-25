from django.urls import path
from . import views

app_name = "ex7"

urlpatterns = [
    # path('', views.cat_str, name='cat_str'),
    path('catstr/', views.CatstrView.as_view(), name='cat_str2'),
]
