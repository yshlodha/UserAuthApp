from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.db import IntegrityError
from django.views.generic.edit import FormView
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout

from custom_auth.forms import NewEmailForm, UpdateProfileForm
from custom_auth.data import *

class HomeView(FormView):
    form_class = UpdateProfileForm
    template_name = 'user_profile.html'

    def get_context_data(self, *args, **kwargs):
        """
        :param args:
        :param kwargs:
        :return:
        """
        context =  super(HomeView, self).get_context_data(*args, **kwargs)
        add_email_form = NewEmailForm()
        context['user'] = self.request.user
        context['add_email_form'] = add_email_form
        return context

    def get(self, request, *args, **kwargs):
        return super(HomeView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        request = self.request
        primary_email = form.cleaned_data.get('primary_email')
        all_emails = get_user_emails(request.user)
        if not primary_email in all_emails:
            form.errors['primary_email'] = form.error_class(['No such email is add by you with your emails.'])
            return self.form_invalid(form)
        set_primary(request.user, primary_email)
        return HttpResponseRedirect(reverse('home'))

    def form_invalid(self, form):
        """
        :param form:
        :return:
        """
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)


class AddEmailView(FormView):
    """
    """
    template_name = 'add_new_email.html'
    form_class = NewEmailForm

    def get(self, request, *args, **kwargs):
        """
        """
        return super(AddEmailView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        """
        :param form:
        :return:
        """
        request = self.request
        new_email = form.cleaned_data.get('new_email')
        try:
             create_user_extra_email(request.user,  new_email)
        except IntegrityError:
            form.errors['new_email'] = form.error_class(['This email is already been used.'])
            return self.form_invalid(form)
        return HttpResponseRedirect(reverse('home'))

    def form_invalid(self, form):
        """
        :param form:
        :return:
        """
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)
