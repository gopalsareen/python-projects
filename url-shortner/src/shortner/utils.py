import random
import string
from django.conf import settings

SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 15)


def code_geneartor(size=SHORTCODE_MIN, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def create_shortcode(context, size=SHORTCODE_MIN):
    new_code = code_geneartor(size=size)

    objClass = context.__class__  

    records = objClass.objects.filter(shortcode=new_code)

    if records.exists():
        return  create_shortcode(size=size)
    return new_code   