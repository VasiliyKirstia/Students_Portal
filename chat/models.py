from django.db import models
from django.contrib.auth.models import User
from django.utils.html import escape


class Room(models.Model):
    id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=150, verbose_name='название')

    members = models.ManyToManyField(User,
                                     through='Membership',
                                     verbose_name='участники')

    def __add_message(self, sender, message):
        m = Message(room=self, author=sender, message=escape(message))
        m.save()
        return m

    def say(self, sender, message):
        return self.__add_message(sender, message)

    def join(self, user):
        Membership.objects.create(room=self, user=user)

    def leave(self, user):
        Membership.objects.filter(room=self).filter(user=user)[0].delete()

    def messages(self, after_pk=None, after_date=None):
        m = Message.objects.filter(room=self)
        if after_pk:
            m = m.filter(pk__gt=after_pk)
            return m.order_by('pk')
        if after_date:
            m = m.filter(timestamp__gte=after_date)
            return m.order_by('timestamp')


    def last_message_id(self):
        m = Message.objects.filter(room=self).order_by('pk')
        if m:
            return m[0].id - 1
        else:
            return 0

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'комната'
        verbose_name_plural = 'комнаты'


class Membership(models.Model):
    room = models.ForeignKey(Room)
    user = models.ForeignKey(User)


class Invite(models.Model):
    id = models.AutoField(primary_key=True)

    room = models.ForeignKey(to=Room,
                             related_name='invites',
                             verbose_name='комната')

    to = models.ForeignKey(to=User,
                           related_name='invites',
                           verbose_name='приглашенный')

    def to_json(self):
        return {
            'title': self.room.title,
            'room_id': self.room.id,
        }

    class Meta:
        verbose_name = 'приглашение'
        verbose_name_plural = 'приглашения'


class Message(models.Model):
    id = models.AutoField(primary_key=True)

    room = models.ForeignKey(Room, verbose_name='комната')

    author = models.ForeignKey(User, related_name='messages', verbose_name='автор')

    message = models.CharField(verbose_name='текст сообщения')

    timestamp = models.DateTimeField(auto_now=True, verbose_name='время отправки')

    def to_json(self):
        return {
            'date': self.timestamp,
            'author': "{} {}".format(self.author.first_name, self.author.last_name),
            'message': self.__str__(),
        }

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'