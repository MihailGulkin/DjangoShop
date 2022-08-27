from django.forms import ModelForm
from django import forms
from .models import Product, Bucket


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'availability', 'group', 'img']



class BucketForm(ModelForm):
    class Meta:
        model = Bucket
        fields = ['quantity']