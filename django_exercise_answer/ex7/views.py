from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy

from .forms import ImpForm

def cat_str(request):
    if request.method == "POST":
        form = ImpForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['msg'] == "CLEAR":
                request.session.clear()
            else:
                request.session['msg'] += form.cleaned_data['msg']
            return redirect('ex7:cat_str')
        else:
            return render(request, 'cat_str.html', {'form': form})
    else:
        if not request.session.get('msg'):
            request.session['msg'] = ""
        return render(request, 'cat_str.html', {'form': ImpForm()})

class CatstrView(generic.FormView):
    template_name = 'cat_str.html'
    form_class = ImpForm
    success_url = reverse_lazy('ex7:cat_str2')

    def get(self, request, *args, **kwargs):
        if not request.session.get('msg'):
            request.session['msg'] = ""
        return super().get(request, *args, **kwargs)
    
    def form_valid(self, form):
        msg = form.cleaned_data['msg']
        if msg == "CLEAR":
            self.request.session.clear()
        else:
            self.request.session['msg'] += msg
        return super().form_valid(form)
