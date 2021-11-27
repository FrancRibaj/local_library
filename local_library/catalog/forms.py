
from .models import Book
from django import forms
import datetime
from django.core.exceptions import ValidationError


class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).",widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    def clean_renewal_date(self):
        cleaned_date = self.cleaned_data['renewal_date']

        # Check if a date is not in the past.
        if cleaned_date < datetime.date.today():
            raise ValidationError('Invalid date - renewal in past')

        # Check if a date is in the allowed range (+4 weeks from today).
        if cleaned_date > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError('Invalid date - renewal more than 4 weeks ahead')

        # Remember to always return the cleaned data.
        return cleaned_date


class BookModelForm(forms.ModelForm):

    class Meta:
        model = Book
        # fields = '__all__'
        fields = ('title', 'isbn', 'author', 'summary','genre')


class AuthorForm(forms.ModelForm):

    first_name =forms.CharField(max_length=100)
    last_name = forms. CharField(max_length=100)
    date_of_birth = forms.  DateField(max_length=False,widget=forms.widgets.DateInput(attrs={'type': 'date'})
    date_of_death = forms.DateField(max_length= False,widget=forms.widgets.DateInput(attrs={'type': 'date'})
    def clean_date_of_death(self):
        date_of_birth = self.cleaned_data['date_of_birth']
        date_of_death= self.cleaned_data['date_of_death']
        if date_of_death < date_of_birth:
            raise ValidationError('Date of death cannot be prior date of birth.')
        return date_of_death
