from django.forms import ValidationError


def validate_type(value):
    invalid_types = [
        'application/x-msdownload',
        'application/x-elf',
        'application/x-sh',
        'application/x-executable',
        'application/octet-stream',
    ]
    print(str(value.file.content_type))
    if value.file.content_type in invalid_types:
        raise ValidationError(u'File type not supported!')
