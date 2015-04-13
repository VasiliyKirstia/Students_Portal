from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

    id = models.AutoField(primary_key=True)

    user = models.OneToOneField(to=User, related_name='profile')

    dr = models.DateField(verbose_name='день рождения')

    room_number = models.IntegerField(verbose_name='комната')

    photo = models.ImageField(width_field=150, height_field=250, verbose_name='фото')

    is_free = models.BooleanField(verbose_name='ищу вторую половинку')