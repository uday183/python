# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Post(models.Model):
	title=models.CharField(max_length=200)
	body=models.TextField()
	date=models.DateTimeField()

	def __str__(self):
		return self.title


class Details(models.Model):
	name=models.CharField(max_length=200)
	age =models.CharField(max_length=200)
	company=models.CharField(max_length=200)
	place=models.CharField(max_length=200)
	designation=models.CharField(max_length=200)

	def __str__(self):
		return self.name


class Country(models.Model):
	name=models.CharField(max_length=30)

	def __str__(self):
		return self.name

class City(models.Model):
	country = models.ForeignKey(Country, on_delete=models.CASCADE)
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name

class Person(models.Model):
	name = models.CharField(max_length=100)
	birthdate=models.DateField(null=True,blank=True)
	country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
	city =models.ForeignKey(City,on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.name
		














