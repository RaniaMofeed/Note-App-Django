import datetime
from entries.models import Entry

from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class EntryForm(forms.ModelForm):
    title=forms.CharField(max_length=20,required=True)
    content=forms.Textarea()

    class Meta:
        model=Entry
        fields=['title','content']
   