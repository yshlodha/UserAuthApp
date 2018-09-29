from django.conf import settings
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import check_password

User = get_user_model()

class AuthBackend(ModelBackend):
    '''
    '''

    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
                # Create a new user. There's no need to set a password
                # because only the password from settings.py is checked.
             return None

        if user.is_blocked():
            raise ValidationError('User is Blocked. Please Try after sometime')
        if check_password(password, user.password):
            return user
        else:
            self.block_counter(user)
        return None

    def block_counter(self, user):
        '''
        :param user:
        :return:
        '''
        if not user.is_block:
            user.block_count += 1
            if user.block_count >= 3:
                user.is_block = True
                user.block_date_time = timezone.now()
            user.save()



    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None