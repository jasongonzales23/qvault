from django.contrib import admin
from contactform.models import Contact, FollowUp
import datetime

class FollowUpAdminInline(admin.StackedInline):
    model = FollowUp

class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'i_am', 'application_date','contacted', 'status')
    
        
    def contacted(self, obj):
        #self is COntactAdmin
        #obj apears to be the unicode returned from Contact
        this = FollowUp.objects.filter(contact = obj)
        this = this.latest('date')
        return this
    contacted.admin_order_field = 'i_am'
    
    list_filter = ('i_am',)

    
    inlines = [
        FollowUpAdminInline,
    ]

class FollowUpAdmin(admin.ModelAdmin):
    list_display = ('contact', 'date', 'notes')
    search_fields = ('contact',)
    
    
admin.site.register(Contact, ContactAdmin)
admin.site.register(FollowUp, FollowUpAdmin)