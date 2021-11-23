from django import forms
import datetime
from django.core.exceptions import ValidationError


class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).",initial = datetime.today)

    def clean_renewal_date(self):
        cleaned_date = self.cleaned_data['renewal_date']

        # Check if a date is not in the past.
        if cleaned_date < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        # Check if a date is in the allowed range (+4 weeks from today).
        if cleaned_date > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        # Remember to always return the cleaned data.
        return cleaned_date

