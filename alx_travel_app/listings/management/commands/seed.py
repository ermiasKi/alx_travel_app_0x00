from django_seed import Seed
import random
from time import timezone
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from listings.models import Listing, Booking, Review

User = get_user_model()
class seederclass(BaseCommand):

    def model_seeder(self, *args, **kwargs):
        seed = Seed.seeder()

        # seed.add_entity(User, 10)
        # seed.add_entity(Listing, 10)
        # seed.add_entity(Booking, 10)
        seed.add_entity(Review, 10, {
    "rating": lambda x: random.randint(1, 5),
    "created_at": lambda x: timezone.now(),
    "listing": lambda x: random.choice(Listing.objects.all()),
    "user": lambda x: random.choice(User.objects.all()),
})

        seed.execute()

