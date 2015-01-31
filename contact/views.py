from django.shortcuts import render
from contact.forms import ContactForm
from django.core.mail import send_mail
from context_processors import site_settings_processor
from utilities import ContactFormProcessor, ExampleFormProcessor

from django.template.context import RequestContext

# Create your views here.
def contact(request):
	context_dictionary = {}
	ContactFormProcessor(request, context_dictionary)
	return(render(request, 'contact/contact.html', context_dictionary))

def example_form(request):
	context_dictionary = {}
	ExampleFormProcessor(request, context_dictionary)
	return(render(request, 'contact/example_form.html', context_dictionary))