from django import forms
from courier.models import Order

class TicketForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('orderid',)
