from django import forms
from .models import TestModel


class TestForm(forms.ModelForm):
    class Meta:
        model = TestModel
        fields = [
            'name',
            'email',
            'nbr',
        ]

    def clean_name(self, *a, **kw):
        name = self.cleaned_data.get('name')
        if "ayb" in name:
            return name
        else:
            raise forms.ValidationError("title of aybat")


class TestRawForm(forms.Form):
    title = forms.CharField(max_length=10)
    age = forms.IntegerField()
