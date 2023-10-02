from django.forms.models import BaseInlineFormSet


class LanguagesProfileForm(BaseInlineFormSet):
    def _construct_form(self, i, **kwargs):
        form = super(LanguagesProfileForm, self)._construct_form(i, **kwargs)
        if i < 1:
            form.empty_permitted = False
        return form