from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    '''
    '''
    block_count = models.IntegerField(default=0)
    is_block = models.BooleanField(default=False)
    block_date_time = models.DateTimeField(null=True, blank=True)

    USERFIELD_NAME = 'email'

    def __str__(self):
        return self.email

    def is_blocked(self):
        '''
        check if user is blocked or not
        :return:
        '''
        if self.is_block:
            now = timezone.now()
            last_block = self.block_date_time
            total_time_user_blocked = now - last_blocked
            if total_time_user_blocked <= 300:
                return True
            else:
                self.block_date_time = None
                self.is_block = False
                self.save()
                return False
        return False
