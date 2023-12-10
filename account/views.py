from django.shortcuts import render
from .forms import RegistrationForm
from django.shortcuts import redirect


def account_register(request):
    if request.user.is_authenticated():
        return redirect('/')

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.set_password = form.cleaned_data['password']
            user.is_active = False
            user.save()


