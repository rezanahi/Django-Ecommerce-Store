from django.urls import path
from .views import account_register, account_activate, dashboard
from django.contrib.auth.views import LoginView
from .forms import UserLoginForm

app_name = 'account'

urlpatterns = [
    path('register/', account_register, name='register'),
    path('activate/<slug:uidb64>/<slug:token>/', account_activate, name='activate'),
    path('dashboard/', dashboard, name='dashboard'),
    path('login/', LoginView.as_view(template_name='account/registration/login.html',
                                     form_class=UserLoginForm), name='login'),
]

