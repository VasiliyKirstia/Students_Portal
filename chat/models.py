from django.db import models
from django.contrib.auth.models import User
from django.utils.html import escape

class Room(models.Model):

    id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=150, verbose_name='название')

    members = models.ManyToManyField(User,
                                     through='Membership',
                                     verbose_name='участники')

    last_recv = models.DateTimeField(auto_now=True)

    def __add_message(self, type, sender, message=None):
        """Generic function for adding a message to the chat room"""
        m = Message(room=self, type=type, author=sender, message=escape(message))
        m.save()
        return m

    def say(self, sender, message):
        """Say something in to the chat room"""
        return self.__add_message('m', sender, message)

    def join(self, user):
        """A user has joined"""
        Membership.objects.create(room=self, user=user)
        if Membership.objects.filter(room=self).filter(user=user).count() == 1:
            return self.__add_message('j', user)

    def leave(self, user):
        """A user has leaved"""
        Membership.objects.filter(room=self).filter(user=user)[0].delete()
        if Membership.objects.filter(room=self).filter(user=user).count() == 0:
            return self.__add_message('l', user)

    def messages(self, after_pk=None, after_date=None):
        """List messages, after the given id or date"""
        m = Message.objects.filter(room=self)
        if after_pk:
            m = m.filter(pk__gt=after_pk)
        if after_date:
            m = m.filter(timestamp__gte=after_date)
        return m.order_by('pk')

    def last_message_id(self):
        """Return last message sent to room"""
        m = Message.objects.filter(room=self).order_by('pk')
        if m:
            return m[0].id - 1
        else:
            return 0

    def __str__(self):
        return 'Chat for %s %d' % (self.content_type, self.object_id)

    class Meta:
        ordering = ['-last_recv']
        verbose_name = 'комната'
        verbose_name_plural = 'комнаты'


class Membership(models.Model):
    room = models.ForeignKey(Room)
    user = models.ForeignKey(User)


MESSAGE_TYPE_CHOICES = (
    ('s', 'system'),
    ('a', 'action'),
    ('m', 'message'),
    ('j', 'join'),
    ('l', 'leave'),
    ('n', 'notification')
)


class Message(models.Model):

    id = models.AutoField(primary_key=True)

    room = models.ForeignKey(Room, verbose_name='комната')

    type = models.CharField(max_length=1, choices=MESSAGE_TYPE_CHOICES, verbose_name='тип')

    author = models.ForeignKey(User, related_name='messages', blank=True, null=True, verbose_name='автор')

    message = models.CharField(max_length=255, blank=True, null=True, verbose_name='текст сообщения')

    timestamp = models.DateTimeField(auto_now=True, verbose_name='время отправки')

    def to_json(self):
        return {
            'id': self.pk,
            'author': "{} {}".format(self.author.first_name, self.author.last_name),
            'message': self.__str__(),
            'type': self.type
        }

    def __str__(self):
        """Each message type has a special representation, return that representation.
        This will also be translator AKA i18l friendly."""
        if self.type == 's':
            return u'SYSTEM: %s' % self.message
        if self.type == 'n':
            return u'NOTIFICATION: %s' % self.message
        elif self.type == 'j':
            return 'JOIN: %s' % self.author
        elif self.type == 'l':
            return 'LEAVE: %s' % self.author
        elif self.type == 'a':
            return 'ACTION: %s > %s' % (self.author, self.message)
        return self.message

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'