from django.shortcuts import render
from contact.forms import ContactForm
from django.core.mail import send_mail
from context_processors import site_settings_processor
from utilities import ContactFormProcessor

from django.template.context import RequestContext

# Create your views here.
def contact(request):
	context_dictionary = {}
	ContactFormProcessor(request, context_dictionary)
	if request.method == 'POST':
		if 'form_errors' in context_dictionary:
			return(render(request, 'contact/contact.html', context_dictionary))
		else:
			return(render(request, 'contact/contact.html', context_dictionary))
	else:
		return(render(request, 'contact/contact.html', context_dictionary))