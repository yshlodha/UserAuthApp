from django.urls import path, include, re_path

from custom_auth.views import *

urlpatterns = [
    re_path(r'^login/$', LoginView.as_view(), name='login'),
    re_path(r'^signup/$', SignupView.as_view(), name='signup'),
    re_path(r'^profile/$', HomeView.as_view(), name='home'),

]