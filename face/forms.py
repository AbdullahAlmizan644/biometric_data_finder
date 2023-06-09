from django import forms
from .models import PersonData

class PersonDataForm(forms.ModelForm):
    class Meta:
        model=PersonData
        fields='__all__'
        widgets={
            'gender': forms.RadioSelect,
        }


class FaceImageForm(forms.Form):
    image=forms.ImageField()