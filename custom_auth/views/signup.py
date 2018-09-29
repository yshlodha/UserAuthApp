from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.db import IntegrityError
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout


from custom_auth.forms import *
from custom_auth.data import create_user
# Create your views here.

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
        try:
            create_user(email, password, username=username)
        except IntegrityError:
            form.errors['username'] = form.error_class(['Please Provide Unique Email and Username'])
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