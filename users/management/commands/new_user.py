from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='user@test.com',
            first_name='New',
            last_name='User',


        )
        user.set_password('user123')
        user.save()