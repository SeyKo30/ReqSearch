from django import forms
from .models import Company, UploadedDocument
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TextInputForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)

class CompanyForm(forms.ModelForm):
    responsible_person = forms.CharField(max_length=100, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    address = forms.CharField(max_length=255, required=False)

    class Meta:
        model = Company
        fields = ['name', 'EDR', 'responsible_person', 'phone_number', 'address']

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

class DocumentForm(forms.ModelForm):
    class Meta:
        model = UploadedDocument
        fields = ['file']
