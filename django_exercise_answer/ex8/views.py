from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm


def my_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()  # ログイン対象の user (Userクラス)
            if user:
                login(request, user)    # ログイン
                return redirect('../login_ok/')  # ログイン完了ページへリダイレクト
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def login_ok(request):
    return render(request, 'login_ok.html')


def my_logout(request):
    logout(request)
    return redirect('ex8:logout_ok')


def logout_ok(request):
    return render(request, 'logout_ok.html')


class MyLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

class MyLoginOKView(TemplateView):
    template_name = 'login_ok.html'


class MyLogoutView(LogoutView):
    pass


class MyLogoutOKView(TemplateView):
    template_name = 'logout_ok.html'
