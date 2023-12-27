from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _
# from django_countries.fields import CountryField
from django.db import models
from django.core.mail import send_mail


class CustomModelManager(BaseUserManager):
    def create_superuser(self, email, user_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_superuser', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')

        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, password, **other_fields)

    def create_user(self, email, user_name, password, **other_fields):
        if not email:
            raise ValueError(_('You must provide an email address'))
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class UserBase(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email_address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    about = models.TextField(_('about'), max_length=500, blank=True)
    ####

    phone_number = models.CharField(max_length=15, blank=True)
    postcode = models.CharField(max_length=12, blank=True)
    address_line_1 = models.CharField(max_length=150, blank=True)
    address_line_2 = models.CharField(max_length=150, blank=True)
    town_city = models.CharField(max_length=150, blank=True)
    ####
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = CustomModelManager()

    REQUIRED_FIELDS = ['user_name']
    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = 'account'
        verbose_name_plural = 'accounts'

    def email_user(self, subject, message):
        send_mail(subject=subject, message=message, from_email='', recipient_list=[self.email], fail_silently=False)

    def __str__(self):
        return self.user_name