# from django import forms
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit
# from .models import Profile

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('firstName', 'lastName', 'email', 'phoneNumber', 'department', 'bio')

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_method = 'post'
#         self.helper.add_input(Submit('submit', 'save person'))

from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model 

User = get_user_model()

class SignupForm(UserCreationForm):
    firstname = forms.CharField(max_length=30, required=False, help_text='optional')
    lastname = forms.CharField(max_length=30, required=False, help_text='optional')
    email = forms.EmailField(max_length=100, help_text='required')
    class meta:
        model = User 
        fields = ['username', 'firstname', 'lastname', 'email', 'password1', 'password2']