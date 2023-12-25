from django import forms

class PersonForm(forms.Form):
    name = forms.CharField(label='名前')
    age = forms.IntegerField(label='年齢')
    blood_type = forms.ChoiceField(label='血液型',
        choices=(
            ('A', 'A型'),
            ('B', 'B型'),
            ('AB', 'AB型'),
            ('O', 'O型'),
            ('他', "その他"),
        )
    )
