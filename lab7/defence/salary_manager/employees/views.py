from django.shortcuts import render
from .models import Employee
from django.http import JsonResponse

def employee(request):
    employees = Employee.objects.all()
    data = {'employee': list(employees.values())}
    return JsonResponse(data)
