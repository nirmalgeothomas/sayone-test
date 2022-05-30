from django.forms import ModelForm
from .models import Order


class EventForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
