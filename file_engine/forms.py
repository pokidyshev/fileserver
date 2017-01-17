from django import forms

from .models import Document


EXPIRE_CHOICES = [
    ('1', '1 minute'),
    ('30', '30 minutes'),
    ('60', '1 hour'),
    ('600', '10 hours'),
    ('1440', '1 day'),
    ('7200', '5 days'),
]


class DocumentForm(forms.ModelForm):
    expire_in = forms.ChoiceField(
        choices=EXPIRE_CHOICES,
    )

    class Meta:
        model = Document
        fields = ('description', 'document',)
