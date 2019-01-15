# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from StudentLogin.forms import UserForm
from django.contrib.auth.models import User
from django.views.generic import TemplateView, CreateView, DetailView
from StudentLogin.models import Tickets
from StudentLogin.forms import TicketForm
from django.urls import reverse_lazy
# Create your views here.



class home(TemplateView):
    template_name = 'StudentLogin/home.html'

class index(TemplateView):
    template_name = 'StudentLogin/index.html'

class ProfileDetailView(DetailView):
    model = User
    template_name = 'StudentLogin/update.html'

class Ticket(CreateView):
    model = Tickets
    form_class = TicketForm
    template_name = 'StudentLogin/ticket.html'
    success_url = reverse_lazy('index')


def register(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.user = request.user
            user.set_password(user.password)
            user.save()
            registered = True
            if registered == True:
                return HttpResponseRedirect('/student/info/%d'%user.id)
            else:
                return HttpResponse("Username already in use.")
    else:
        user_form = UserForm()
    return render(request,'StudentLogin/register.html',{})
