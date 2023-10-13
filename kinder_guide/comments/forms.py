from django import forms
from django.utils.translation import gettext_lazy as _

from .constants import CHOICES
from .models import Review


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
