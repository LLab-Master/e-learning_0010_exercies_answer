from django.urls import path
from . import views

app_name = "ex5"

urlpatterns = [
    path('add_emp1/', views.add_emp1, name='add_emp1'),
    path('add_emp1_end/', views.add_emp1_end, name='add_emp1_end'),
    path('list_emp/', views.EmpListView.as_view(), name='list_emp'),
    path('detail_emp/<int:pk>', views.EmpDetailView.as_view(), name='detail_emp'),
    path('add_emp2/', views.EmpCreateView.as_view(), name='add_emp2'),
    path('update_emp/<int:pk>', views.EmpUpdateView.as_view(), name='update_emp'),
    path('update_emp_end/', views.EmpUpdateEndView.as_view(), name='update_emp_end'),
    path('delete_emp/<int:pk>', views.EmpDeleteView.as_view(), name='delete_emp'),
    path('delete_emp_end/', views.EmpDeleteEndView.as_view(), name='delete_emp_end'),
]
