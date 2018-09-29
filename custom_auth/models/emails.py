from django.db import models
from custom_auth.models import CustomUser as User


class EmailAddress(models.Model):
    '''
    '''
    user = models.ForeignKey(User, models.CASCADE)
    email_address = models.EmailField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return self.email_address

    def save(self, *args, **kwargs):
        if self.is_primary:
            user.email = self.email_address
            user.save()
        super(EmailAddress, self).save(*args, **kwargs)

    class Meta:
        unique_together = ('user', 'email_address')