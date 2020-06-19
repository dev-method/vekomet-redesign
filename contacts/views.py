from django.shortcuts import render
from contacts.models import ContactsSeo, ContactsText
from vekomet_redesign import settings

# Create your views here.
def contacts(request):
    contacts_flag = "current"
    seo = ContactsSeo.objects.all()
    text = ContactsText.objects.all()
    return render(request, 'contacts/{}/contacts.html'.format(settings.TEMP_PREFIX), {'seo': seo, 'text': text, 'contacts_flag': contacts_flag})

def en_contacts(request):
    contacts_flag = "current"
    seo = ContactsSeo.objects.all()
    text = ContactsText.objects.all()
    return render(request, 'contacts/{}/en-contacts.html'.format(settings.TEMP_PREFIX), {'seo': seo, 'text': text, 'contacts_flag': contacts_flag})