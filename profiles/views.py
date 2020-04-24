from django.shortcuts import render, redirect
from profiles.models import Profile
from profiles.forms import ProfileForm, ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    template = 'index.html'
    profile = Profile.objects.all
    return render(request, template, {'profile':profile})

# def about(request):
#     template = 'about.html'
#     return render(request, template, { })

def contact(request):
    template = 'contact.html'
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.GET)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            firstName = form.cleaned_data['firstName']
            lastName = form.cleaned_data['lastName']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, email,['akorir233@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')

    return render(request, template, {'form':form })

def base(request):
    template = 'base.html'
    return render(request, template, { })

def profile(request):
    template = 'profile.html'
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProfileForm
    return render(request, template, {'form':form})
