from django.db import models

from shortner.models import Url

# Create your models here.


class ClickEventManager(models.Manager):
    def create_event(self, instance):
        if isinstance(instance, Url):
            obj, created = self.get_or_create(url=instance)
            obj.count += 1
            obj.save()
            return obj.count
        return None


class ClickEvent(models.Model):
    url = models.OneToOneField(
        Url,
        on_delete=models.CASCADE
    )
    count = models.IntegerField(default=0)
    last_edited = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    objects = ClickEventManager()

    def __str__(self):
        return "{i}".format(i=self.count)