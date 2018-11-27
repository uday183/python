# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from blog.models import Details
# Create your views here.
def index(request):
	return render(request,'personal/home.html' )


def contact(request):

	return render(request,'personal/basic.html', {'content':['If you would like to contact me please send mail, uday@gmail.com']})



