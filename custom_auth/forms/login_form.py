from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=255,
                               widget=forms.EmailInput(attrs={'class': 'form-control', 'name': 'email'}))
    password = forms.CharField(label="Password", max_length=100,
                               widget=forms.PasswordInput())

    def clean(self):
        """
        """
        self.cleaned_data = super(LoginForm, self).clean()
        try:
            user_name = self.cleaned_data['email']
        except KeyError:
            self._errors['email'] = self.error_class(["This field can't be empty."])
        try:
            password = self.cleaned_data['password']
        except KeyError:
            self._errors['password'] = self.error_class(["This field can't be empty."])

        return self.cleaned_data