from django.apps import AppConfig


class ListingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'listings'


import django.utils.timezone as timezone

# Patch make_aware to ignore is_dst if passed
old_make_aware = timezone.make_aware

def safe_make_aware(value, tz=None, is_dst=None):
    return old_make_aware(value, tz)

timezone.make_aware = safe_make_aware
