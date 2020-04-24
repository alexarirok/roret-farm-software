from django import forms 
from profiles.models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['firstName', 'lastName', 'email', 'phoneNumber', 'department', 'bio'] 

class ContactForm(forms.Form):
    firstName = forms.CharField(max_length=30, required=True, help_text='required')
    lastName = forms.CharField(max_length=30, required=True, help_text='required')
    email = forms.EmailField(max_length=100, required=True, help_text='required')
    subject = forms.CharField(max_length=50, help_text='optional')
    message = forms.CharField(widget=forms.Textarea, required=True)