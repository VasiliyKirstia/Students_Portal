from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

    id = models.AutoField(primary_key=True)

    user = models.OneToOneField(to=User, related_name='profile')

    dr = models.DateField(verbose_name='день рождения')

    room_number = models.IntegerField(verbose_name='комната')

    is_free = models.BooleanField(default=False, verbose_name='ищу вторую половинку')