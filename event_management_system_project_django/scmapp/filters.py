import django_filters
from django_filters import DateFilter, CharFilter

from .models import Event
from .models import *


class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="start_date", lookup_expr='gte')
    end_date = DateFilter(field_name="end_date", lookup_expr='lte')
    category = CharFilter(field_name='category', lookup_expr='icontains')

    class Meta:
        model = Event
        fields = ['description', 'name', 'published']
        exclude = ['image']
