from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView

from app.models import *


class SchoolList(ListView):
    model=School
    context_object_name='schools'
    # ordering=['sname']
    # queryset=School.objects.filter(id=1)
    # template_name='school_list.html'


class StudentList(ListView):
    model=Student
    context_object_name='Students'
    # ordering=['stname']
    # queryset=Student.objects.filter(id=2)
    # template_name='student_list.html'

