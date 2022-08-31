from django.template.defaulttags import register
from web.models import Bucket


@register.filter(name='bucket_sum')
def bucket_sum(bucket: Bucket):
    return sum(item.quantity * item.product.price
               for item in bucket)
