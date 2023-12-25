from django.shortcuts import render
from . import forms

def input1(request):
    if request.method == 'POST':
        form = forms.PersonForm(request.POST)
        if form.is_valid():
            ctx = {
                'name': form.cleaned_data['name'],
                'age': form.cleaned_data['age'],
                'blood_type': form.cleaned_data['blood_type'],
            }
            return render(request, 'show_person1.html', ctx)
        else:
            ctx = {
                'form': form,
            }
            return render(request, 'input_persop1.html', ctx)
    else:
        form = forms.PersonForm()
        ctx = {
            'form': form
        }     
        return render(request, 'input_person1.html', ctx)