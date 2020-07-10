from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmployeeForm
from .models import Employee
# Create your views here.

def employee_list(request, template_name='employee/employee_list.html'):
    employee = Employee.objects.all()
    context = {}
    context['employee_list'] = employee

    return render(request, template_name, context)

def employee_register(request, template_name='employee/employee_register.html'):
    if request.method == 'GET':
        form = EmployeeForm()
        return render(request, template_name, {'form': form})
    else:
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/list')


def employee_update(request, pk, template_name='employee/employee_register.html'):
    employee = get_object_or_404(Employee, pk=pk)
    form = EmployeeForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, template_name, {'form':form})    

def employee_delete(request, pk):
    employee = Employee.objects.get(pk=pk)
    employee.delete()
    return redirect('/list')


# def book_delete(request, pk):
#     book= get_object_or_404(Book, pk=pk)    
#     if request.method=='POST':
#         book.delete()
#         return redirect('book_list')
#     return render(request, template_name, {'object':book})