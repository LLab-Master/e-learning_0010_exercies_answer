from django.urls import path
from . import views

app_name = 'ex8'

urlpatterns = [
    path('login/', views.my_login, name='login'),
    path('login_ok/', views.login_ok, name='login_ok'),
    path('logout/', views.my_logout, name='logout'),
    path('logout_ok/', views.logout_ok, name='logout_ok'),

    path('login2/', views.MyLoginView.as_view(), name='login2'),
    path('login_ok2/', views.MyLoginOKView.as_view(), name='login_ok2'),
    path('logout2/', views.MyLogoutView.as_view(), name='logout2'),
    path('logout_ok2/', views.MyLogoutOKView.as_view(), name='logout_ok2'),    
]
