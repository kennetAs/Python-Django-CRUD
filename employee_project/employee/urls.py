from django.urls import path

from . import views


urlpatterns = [

    path('list', views.employee_list, name='employee_list'),
    path('', views.employee_register, name='employee_register'),
    path('edit/<int:pk>', views.employee_update, name='employee_update'),
    path('delete/<int:pk>', views.employee_delete, name='employee_delete')
]