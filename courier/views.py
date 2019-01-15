# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from courier.models import Order
from courier.forms import TicketForm
from StudentLogin.models import Tickets
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
import smtplib
# Create your views here.
class home(TemplateView):
    template_name = 'courier/home.html'

class Order(CreateView):
    model = Order
    form_class = TicketForm
    template_name = 'courier/order.html'
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        orid = request.POST.get('orderid')
        mail(orid)
        return HttpResponse("Email sent succcessfully")

def mail(orderid):
    tickets = Tickets.objects.get(courierid = orderid)
    print tickets.user.email
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login('sarvanimini@gmail.com','sarvani2410')
    mail.sendmail('sarvanimini@gmail.com',tickets.user.email,"Hello divya")
    mail.close()
    return HttpResponse("Email sent succcessfully")
