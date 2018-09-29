from django.contrib.auth.hashers import make_password

from custom_auth.models import *


def create_user(email, password, username=None):
    """
    :param email:
    :param password:
    :param username:
    :return:
    """
    password = make_password(password)
    user = CustomUser.objects.create(email=email, password=password,
                                     username=username, is_active=True, is_staff=True)

    create_user_extra_email(user, email, is_primary=True)


def create_user_extra_email(user, email_address, is_primary=False):
    """
    :param user:
    :param email_address:
    :param is_primary:
    :return:
    """
    emails = EmailAddress.objects.create(user=user, email_address=email_address, is_primary=is_primary)
    return emails


def get_user_emails(user):
    """
    :param user:
    :return:
    """
    emails = EmailAddress.objects.filter(user=user).values_list('email_address', flat=True)
