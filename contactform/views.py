from django.conf.urls.defaults import *
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from contactform.models import ContactForm
from django.core.context_processors import csrf
from django.core import mail
import urllib
import urllib2
import urlparse
import string
import models

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']            
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
        
            subject = 'Thanks'
            message = 'Hi ' + first_name
            sender = 'info@q-vault.com'
            recipients = ['jason.gonzales23@gmail.com' , email ]
        
            from django.core.mail import send_mail
            send_mail(subject, message, sender, recipients, fail_silently=False)
            new_contact = form.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()
        
    return render_to_response('contact.html',
        {'form': form,},
        context_instance=RequestContext(request)
    )

