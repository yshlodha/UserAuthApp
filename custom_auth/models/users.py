from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    '''
    '''
    block_count = models.IntegerField(default=0)
    block_date_time = models.DateTimeField(null=True, blank=True)

    USERFIELD_NAME = 'email'

    def __str__(self):
        return self.email