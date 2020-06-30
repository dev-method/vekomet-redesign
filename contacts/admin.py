from django.contrib import admin
from contacts.models import ContactsText, ContTextAdmin
from contacts.models import ContactsSeo, ContactsBanner, ContactsBannerAdmin

# Register your models here.
admin.site.register(ContactsSeo)
admin.site.register(ContactsText, ContTextAdmin)