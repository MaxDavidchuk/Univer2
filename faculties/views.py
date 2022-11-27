from django.shortcuts import render, redirect
from .forms import FacultyForm
from .models import Faculty


def index(request):
	return  render(request, 'faculties/index.html', {})


def create(request):
	transit_data = dict()
	if request.method == 'GET':
		faculty_form = FacultyForm()
		return  render(request, 'faculties/create.html', {'faculty_form': faculty_form})
	elif request.method == 'POST':
		faculty_form = FacultyForm(request.POST, request.FILES)
		faculty_form.save()
		return redirect('/faculties')


def details(request, fid: int):
	return  render(request, 'faculties/details.html', {})


def edit(request, fid: int):
	return  render(request, 'faculties/edit.html', {})


def delete(request, fid: int):
	return  render(request, 'faculties/delete.html', {})