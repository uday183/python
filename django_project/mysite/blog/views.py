# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from blog.models import Details
from django.forms import ModelForm
import pdb
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


# Create your views here.
class DetailModelForm(ModelForm):
	class Meta:
		model=Details
		fields=['name','age','company','place','designation']

def details_of_user(request):
	
	data=Details.objects.all()
	return render(request, 'blog/details.html', {'data':data})

def create_details(request):
	#pdb.set_trace()
	if request.method == 'POST':
		name= request.POST['username']
		age= request.POST['age']
		company= request.POST['company']
		place= request.POST['place']
		designation= request.POST['designation']
		Details.objects.create(name=name,age=age,company=company,place=place,designation=designation)
		return redirect('details')
	return render(request,'blog/includes/de_cre.html')


@csrf_exempt
def edit_details(request):

	pk = request.POST.get('pk')
	name = request.POST.get('name')
	age = request.POST.get('age')
	operation=request.POST.get("operation")
	details_obj = Details.objects.get(pk= pk)
	if operation=='1':
		details_obj.name = name
		details_obj.age = age
		details_obj.save()
	else:
		Details.objects.get(pk= pk).delete()
	return JsonResponse({"status":True})

	# return render(request,'blog/include/edit.html' ,{'obj':obj})

def edit(request):
	if request.method == 'GET':
		
		pk=request.GET.get('edit_id')
		edit_data=Details.objects.filter(pk=pk)
		return render(request,'blog/includes/edit.html',{'edit_data':edit_data[0]})
	if request.method == 'POST':
		edit_pk=request.POST.get('edit_id')
		save_data=Details.objects.get(pk=edit_pk)
		name = request.POST.get('name')
		age = request.POST.get('age')
		place = request.POST.get('place')
		company = request.POST.get('company')
		designation = request.POST.get('designation')
		save_data.name= name
		save_data.age=age
		save_data.place= place
		save_data.designation= designation
		save_data.company = company
		save_data.save()
	return redirect('details')


def delete(request):
	if request.method == 'GET':
		pk=request.GET.get('delete_id')
		delete_data=Details.objects.get(pk=pk)
		delete_data.delete()
	return redirect('details')


























