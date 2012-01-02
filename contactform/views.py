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
        
            subject = 'Thanks for Applying to Q-Vault'
            message = 'Hi ' + first_name + ', \nThanks for applying to be a member of Q-Vault! \nThis email isn\'t from an actual human, I am just some software. My only job is to let you know that one of our experienced staff (a human!) will be contacting you within the next 24 hours. Be very excited, Q-Vault is awesome. \nCheers!\nThe Q-Vault Bot'
            sender = 'info@q-vault.com'
            recipients = [ email ]
        
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

