from django import forms
from Regestrationapp.models import regestration



class regestrationForm(forms.ModelForm):
    class Meta:
        model=regestration
        fields="__all__"
