from .models import *
import django_filters


class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = ['product', 'status', 'date_created']
