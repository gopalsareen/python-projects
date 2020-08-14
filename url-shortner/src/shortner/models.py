from django.db import models
from django.conf import settings
from .utils import create_shortcode
from .validators import validate_url

# from django.core.urlresolvers import reverse
from django_hosts.resolvers import reverse
# Create your models here.

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)

class UrlManager(models.Manager):
    def active(self, *args, **kwargs):
        records = Url.objects.filter(active=False)
        return records
    def refresh_shortcodes(self):
        records = Url.objects.all()

        for record in records:
            record.shortcode = create_shortcode(record)
            record.save()

class Url(models.Model):
    url = models.CharField(max_length=220, unique=True, validators=[validate_url])
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    last_edited = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    objects = UrlManager()

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)

            if "http" not in self.url:
                self.url = "http://" + self.url

        super(Url, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
         return str(self.url)
    
    def get_short_url(self):

        url_path = reverse("shortcode", kwargs = {"shortcode":self.shortcode}, host='www', scheme='http')
        return url_path