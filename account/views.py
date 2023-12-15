from django.shortcuts import render
from .forms import RegistrationForm
from django.shortcuts import redirect
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from .token import account_activation_token


def account_register(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.set_password = form.cleaned_data['password']
            user.is_active = False
            user.save()
            # email setup
            site = get_current_site(request)
            subject = "Active your account"
            message = render_to_string(template_name='account/registration/account_activation_email.html'
                                        ,context={'user': user,
                                                  'domain': site.domain,
                                                  'uid': urlsafe_base64_decode(force_bytes(user.pk)),
                                                  'token': account_activation_token.make_token(user)})
            user.email_user(subject=subject, message=message)

    else:
        form = RegistrationForm()
        return render(request, template_name='account/registration/register.html', context={'form': form})



