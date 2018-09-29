from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.generic.edit import FormView
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout


class HomeView(View):
    def get(self, *args, **kwargs):

        return HttpResponse('Thank You')
