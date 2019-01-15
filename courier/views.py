# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, View
from django.urls import reverse_lazy
from courier.models import Order
from courier.forms import TicketForm
from StudentLogin.models import Tickets
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
import smtplib
import random
# Create your views here.
class home(TemplateView):
    template_name = 'courier/home.html'

'''class Order(TemplateView):
    model = Order
    form_class = TicketForm
    template_name = 'courier/order.html'
    success_url = reverse_lazy('home')'''

def Order(request):
     if request.method == "POST":
         orid = request.POST.get('orderid')
         tickets = Tickets.objects.get(courierid = orid)
         if tickets != None :
             mail = smtplib.SMTP('smtp.gmail.com', 587)
             mail.ehlo()
             mail.starttls()
             mail.login('sarvanimini@gmail.com','sarvani2410')
             mail.sendmail('sarvanimini@gmail.com',tickets.user.email,"Hello divya")
             mail.close()
             u = Order.objects.create(orderid = orid, otp = 234, status = 1)
             u.save()
             return HttpResponse("Email sent succcessfully")
         else :
             u = Order.objects.create(orderid = orid, status = 0, otp = 0)
             u.save()
             return HttpResponseRedirect("/courier/home")
     temp = 'courier/order.html'
     return render(request,temp,{})
