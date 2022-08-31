from django.forms import ModelForm
from .models import Product, Bucket, CommentReviewAboutProduct


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'availability', 'group', 'img']


class BucketForm(ModelForm):
    class Meta:
        model = Bucket
        fields = ['quantity']


class CommentReviewForm(ModelForm):
    class Meta:
        model = CommentReviewAboutProduct
        fields = ['product_pros', 'product_cons', 'product_comment']
