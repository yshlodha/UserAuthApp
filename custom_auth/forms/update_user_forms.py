from django import forms

class NewEmailForm(forms.Form):
    new_email = forms.EmailField(label="New Email", max_length=255,
                               widget=forms.EmailInput(attrs={'class': 'form-control', 'name': 'new_email'}))


    def clean(self):
        """
        """
        self.cleaned_data = super(NewEmailForm, self).clean()
        try:
            user_name = self.cleaned_data['new_email']
        except KeyError:
            self._errors['new_email'] = self.error_class(["This field can't be empty."])

        return self.cleaned_data


class UpdateProfileForm(forms.Form):
    primary_email = forms.EmailField(label="Primary Email", max_length=255,
                               widget=forms.EmailInput(attrs={'class': 'form-control', 'name': 'primary_email'}))