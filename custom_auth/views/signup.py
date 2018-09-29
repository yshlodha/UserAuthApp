from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.db import IntegrityError
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout
from django.contrib.gis.geoip2 import GeoIP2


from custom_auth.forms import *
from custom_auth.data import create_user
# Create your views here.

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_client_location(ip):
    g = GeoIP2()
    if ip=='127.0.0.1':
        location = 'India'
    else:
        location = g.city(ip)['country_name']
    return location

class SignupView(FormView):
    """
    """
    template_name = 'signup.html'
    form_class = SignupForm

    def get(self, request, *args, **kwargs):
        """
        """
        return super(SignupView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        """
        :param form:
        :return:
        """
        request = self.request
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password  = form.cleaned_data.get('password')
        location = get_client_location(get_client_ip(request))
        try:
            create_user(email, password, username=username, location=location)
        except IntegrityError:
            form.errors['username'] = form.error_class(['Please Provide Unique Email and Username'])
            return self.form_invalid(form)
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        return self.form_invalid(form)

    def form_invalid(self, form):
        """
        :param form:
        :return:
        """
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)