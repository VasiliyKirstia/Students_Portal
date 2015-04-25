from django.db import models


class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.IntegerField(unique=True)


class Pack(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.ForeignKey(to=Subject, related_name='pack_set')


class KeyPressTime(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.IntegerField()
    time = models.IntegerField()
    pack = models.ForeignKey(to=Pack, related_name='key_press_time_set')


class KeyReleaseTime(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.IntegerField()
    time = models.IntegerField()
    pack = models.ForeignKey(to=Pack, related_name='key_release_time_set')


class ResearchWorkRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'research_work':
            return 'research_work_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'research_work':
            return 'research_work_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'research_work' or obj2._meta.app_label == 'research_work':
            return True
        return None

    def allow_migrate(self, db, model):
        if db == 'research_work_db':
            return model._meta.app_label == 'research_work'
        elif model._meta.app_label == 'research_work':
            return False
        return None