from django import forms

class ImpForm(forms.Form):
    msg = forms.CharField(label='入力')
