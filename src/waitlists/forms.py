from .models import WaitlistEntry
from django import forms


class WaitlistEntryForm(forms.ModelForm):
    class Meta:
        model = WaitlistEntry
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email.endswith('@mail.ru'):
            raise forms.ValidationError('Can not use mail.ru')
        return email
