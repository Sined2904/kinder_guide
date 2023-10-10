from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Review
from .constants import CHOICES


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'parent']

        labels = {
            'content': _(''),
        }

        widgets = {
            'content': forms.TextInput(),
            'rating': forms.RadioSelect(choices=CHOICES),
        }
