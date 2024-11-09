from .models import WaitlistEntry
from django import forms
from django.utils import timezone


class WaitlistEntryForm(forms.ModelForm):
    class Meta:
        model = WaitlistEntry
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = WaitlistEntry.objects.filter(
            email=email,
            timestamp__day = timezone.now().day
        )
        if qs.count() > 5:
            raise forms.ValidationError('Too much registration of the same email today. Try again tomorrow')
        # if email.endswith('@mail.ru'):
        #     raise forms.ValidationError('Can not use mail.ru')
        return email
