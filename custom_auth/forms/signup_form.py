from django import forms

class SignupForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100,
                               widget=forms.TextInput())
    email = forms.EmailField(label="Email", max_length=255,
                               widget=forms.EmailInput(attrs={'class': 'form-control', 'name': 'email'}))
    password = forms.CharField(label="Password", max_length=100,
                               widget=forms.PasswordInput())

    confirm_password = forms.CharField(label="Confirm Password", max_length=100,
                               widget=forms.PasswordInput())

    def clean(self):
        """
        """
        self.cleaned_data = super(SignupForm, self).clean()
        try:
            username = self.cleaned_data['username']
        except KeyError:
            self._errors['username'] = self.error_class(["This field can't be empty."])
        try:
            user_name = self.cleaned_data['email']
        except KeyError:
            self._errors['email'] = self.error_class(["This field can't be empty."])
        try:
            password = self.cleaned_data['password']
        except KeyError:
            self._errors['password'] = self.error_class(["This field can't be empty."])

        try:
            confirm_password = self.cleaned_data['confirm_password']
        except KeyError:
            self._errors['confirm_password'] = self.error_class(["This field can't be empty."])

        if password != confirm_password:
            self._errors['password'] = self.error_class(["password and confirm password must be same."])
        return self.cleaned_data