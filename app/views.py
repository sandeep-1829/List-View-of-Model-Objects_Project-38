from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView,DetailView,CreateView,UpdateView

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

class SchoolDetail(DetailView):
    model=School
    context_object_name='sclobject'


class SchoolCreate(CreateView):
    model=School
    fields='__all__'


class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'

