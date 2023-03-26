from django import forms
from .models import Child
from .models import Donor

class EditChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['full_name', 'age', 'gender', 'admission_date', 'photo']
        widgets = {
            'admission_date': forms.DateInput(attrs={'type': 'date'}),
        }

class DeleteChildForm(forms.Form):
    confirmation = forms.BooleanField(required=True, help_text="Please confirm that you want to delete this child.")


from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class LoginForm(AuthenticationForm):
    # define any additional form fields you need here
    pass

class SignupForm(UserCreationForm):
    # define any additional form fields you need here
    pass

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ('name', 'email', 'phone', 'amount_donated')



class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=100, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username or Email address'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


from django import forms

from django import forms
from .models import Donation



class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['name', 'email', 'amount']

    def save(self, commit=True):
        donation = super().save(commit=False)
        if commit:
            donation.save()
        return donation






