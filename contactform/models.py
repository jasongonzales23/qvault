from django.db import models
from django.forms import ModelForm
from django import forms
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple

ORIENTATION_CHOICES = (
    ('gay', 'Gay'),
    ('lesbian', 'Lesbian')
)
    
class Contact(models.Model):
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    email= models.EmailField(max_length=255)
    phone= models.CharField(max_length=30, blank=True)
    i_am= models.CharField(max_length=30)
    
    def __unicode__(self):
        return u'%s' % (self.first_name)


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'phone', 'i_am')
        widgets = {
            'i_am': RadioSelect(choices=ORIENTATION_CHOICES, attrs={'class': 'radio',})
        }
        
class FollowUp(models.Model):
    contact=models.ForeignKey('Contact')
    date=models.DateField(auto_now=False)
    notes=models.TextField(max_length=255)
    
    def __unicode__(self):
        return u'%s' % (self.date)
    
    
    