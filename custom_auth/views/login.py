from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout


from custom_auth.forms import *
# Create your views here.

class LoginView(FormView):
    """
    """
    template_name = 'login.html'
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        """
        """
        return super(LoginView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        """
        :param form:
        :return:
        """
        request = self.request
        email = form.cleaned_data.get('email')
        password  = form.cleaned_data.get('password')
        try:
            user = authenticate(username=email, password=password)
        except ValidationError as exc:

            form.errors['email'] = form.error_class([exc.args[0]])
            return self.form_invalid(form)
        else:
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            form.errors['email'] = form.error_class(['invalid user details'])
            return self.form_invalid(form)

    def form_invalid(self, form):
        """
        :param form:
        :return:
        """
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)

def logout_view(request):
    logout(request)
