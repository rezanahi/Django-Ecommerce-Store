from django.shortcuts import render
from .forms import RegistrationForm, UserEditForm
from django.shortcuts import redirect
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from .token import account_activation_token
from shop.models import UserBase
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password


def account_register(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.set_password(form.cleaned_data['password'])
            user.is_active = False
            user.save()
            # email setup
            site = get_current_site(request)
            subject = "Active your account"
            message = render_to_string(template_name='account/registration/account_activation_email.html'
                                        ,context={'user': user,
                                                  'domain': site.domain,
                                                  'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                                                  'token': account_activation_token.make_token(user)})
            user.email_user(subject=subject, message=message)
            return HttpResponse('account registered successfully and activation sent')

    else:
        form = RegistrationForm()
        return render(request, template_name='account/registration/register.html', context={'form': form})


def account_activate(request, uidb64, token):
    uid = force_str(urlsafe_base64_decode(uidb64))
    user = UserBase.objects.get(pk=uid)
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request=request, user=user)
        return redirect('account:dashboard')
    else:
        return render(request, template_name='account/registration/activation_invalid.html')


@login_required
def dashboard(request):
    return render(request, template_name='account/user/dashboard.html')


@login_required
def edit_details(request):
    if request.method == 'POST':
        user_edit = UserEditForm(instance=request.user, data=request.POST)
        if user_edit.is_valid():
            user_edit.save()
    else:
        user_edit = UserEditForm(instance=request.user)
    return render(request, template_name='account/user/edit_details.html', context={'user_form': user_edit})


def delete_user(request):
    user = UserBase.objects.get(user_name=request.user)
    user.is_active = False
    user.save()
    logout(request)
    return redirect('account:delete_confirm')
