from django.core.management.base import BaseCommand, CommandError
from shortner.models import Url

class Command(BaseCommand):
    help = 'Refresh all the url shortcodes.'

    def handle(self, *args, **options):
        print('refreshing shortcodes')
        Url.objects.refresh_shortcodes()
    