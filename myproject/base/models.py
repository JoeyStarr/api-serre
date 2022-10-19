from turtle import title
from venv import create
from django.db import models

# Create your models here.

#serrrrre
class Person(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    firebaseId = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)

class Culture(models.Model):
    intitule = models.CharField(max_length=50, blank=True, null=True)

class Serre(models.Model):
    hashSerre = models.CharField(max_length=250, blank=True, null=True)
    sysSerre = models.JSONField(default=dict, blank=True, null=True)
    dataSerre = models.JSONField(default=dict, blank=True, null=True)
    kultSerre = models.IntegerField(blank=True, null=True)
    person = models.ForeignKey(Person, blank=True, null=True,related_name='serrepers',on_delete=models.CASCADE)
    culture = models.ForeignKey(Culture, blank=True, null=True,related_name='serrekult',on_delete=models.CASCADE)

