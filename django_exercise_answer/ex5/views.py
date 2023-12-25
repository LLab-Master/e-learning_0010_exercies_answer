from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required    # 演習8で追加
from django.contrib.auth.mixins import LoginRequiredMixin    # 演習8で追加

from .models import Emp
from .forms import EmpForm

@login_required   # 演習8で追加
def add_emp1(request):
    if request.method == 'POST':
        form = EmpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ex5:add_emp1_end')
        else:
            ctx = {
                'form': form,
            }
            return render(request, 'add_emp1.html', ctx)
    else:
        form = EmpForm()
        ctx = {
            'form': form
        }
        return render(request, 'add_emp1.html', ctx)

def add_emp1_end(request):
    return render(request, 'add_emp1_end.html')

class EmpCreateView(LoginRequiredMixin, generic.CreateView):  # 演習8で変更
# class EmpCreateView(generic.CreateView):
    template_name = 'add_emp1.html'
    model = Emp
    fields = '__all__'
    success_url = reverse_lazy('ex5:add_emp1_end')

class EmpListView(generic.ListView):
    template_name = 'list_emp.html'
    model = Emp

class EmpDetailView(generic.DetailView):
    template_name = 'detail_emp.html'
    model = Emp

class EmpUpdateView(generic.UpdateView):
    template_name = 'update_emp.html'
    model = Emp
    fields = '__all__'
    success_url = reverse_lazy('ex5:update_emp_end')

class EmpUpdateEndView(generic.TemplateView):
    template_name = 'update_emp_end.html'

class EmpDeleteView(generic.DeleteView):
    template_name = 'delete_emp.html'
    model = Emp
    success_url = reverse_lazy('ex5:delete_emp_end')

class EmpDeleteEndView(generic.TemplateView):
    template_name = 'delete_emp_end.html'
