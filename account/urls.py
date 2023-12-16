from django.urls import path
from .views import account_register, account_activate, dashboard, edit_details
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserLoginForm

app_name = 'account'

urlpatterns = [
    path('register/', account_register, name='register'),
    path('activate/<slug:uidb64>/<slug:token>/', account_activate, name='activate'),
    path('dashboard/', dashboard, name='dashboard'),
    path('login/', LoginView.as_view(template_name='account/registration/login.html',
                                     form_class=UserLoginForm), name='login'),
    path('logout/', LogoutView.as_view(next_page='/account/login/'), name='logout'),
    path('profile/edit/', edit_details, name='edit_details'),
]

