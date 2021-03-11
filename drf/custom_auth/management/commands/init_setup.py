from custom_auth.models import User
from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    help = "Fills the database with initial data"

    def handle(self, *args, **options):
        # Sets up user passwords from fixtures
        call_command('loaddata', 'init_data')
        for user in User.objects.all():
            user.set_password(user.password)
            user.save()
