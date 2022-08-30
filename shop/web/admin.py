from django.contrib import admin
from .models import Product, Bucket, CommentReviewAboutProduct

admin.site.register(Product)
admin.site.register(Bucket)
admin.site.register(CommentReviewAboutProduct)
