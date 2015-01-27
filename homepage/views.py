from django.shortcuts import render
from utilities import ContactFormProcessor

def homepage(request):
	context_dictionary = {}
	ContactFormProcessor(request, context_dictionary)
	return(render(request, 'homepage/index.html', context_dictionary))

def about(request):
	context_dictionary = {}
	ContactFormProcessor(request, context_dictionary)
	return(render(request, 'misc_pages/about.html', context_dictionary))

def products(request):
	context_dictionary = {}
	ContactFormProcessor(request, context_dictionary)
	return(render(request, 'misc_pages/products.html', context_dictionary))

def specials(request):
	context_dictionary = {}
	ContactFormProcessor(request, context_dictionary)
	return(render(request, 'misc_pages/specials.html', context_dictionary))

