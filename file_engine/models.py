from django.db import models
from django.utils import timezone
from datetime import timedelta

from .validators import validate_type


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    # The files will be automatically uploaded to MEDIA_ROOT/documents/
    document = models.FileField(
        upload_to='documents/%Y/%m/%d/',
        validators=[validate_type]
    )
    content_type = models.CharField(max_length=255, default='')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    destruction_at = models.DateTimeField(
        default=timezone.now() + timedelta(hours=1)
    )

    def content(self):
        if self.content_type == 'text/plain':
            with open(self.document.path) as fp:
                return fp.read()
        elif self.content_type.startswith('image'):
            return 'image'
        else:
            return 'Can not display the content'
