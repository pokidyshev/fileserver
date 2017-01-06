import os
from django.utils import timezone
from django.core.management.base import BaseCommand

from file_engine.models import Document


class Command(BaseCommand):
    help = 'delete expired files'

    def handle(self, *args, **options):
        files = Document.objects.all()

        for f in files:
            if f.destruction_at <= timezone.now():
                path = f.document.path
                if os.path.exists(path):
                    os.remove(path)
                f.delete()

        self.stdout.write('Expired files successfully deleted.')
