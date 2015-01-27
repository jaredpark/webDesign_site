from context_processors import site_settings_processor
from django.core.mail import send_mail
from contact.forms import ContactForm

def admin_name():
    return site_settings_processor(None)['admin_name']
    
def ContactFormProcessor(request, context_dictionary):
	if request.method == 'POST':
		if 'contact' in request.POST:
			# create a form instance and populate it with data from the request:
			contact_form = ContactForm(request.POST)
			# check whether it's valid:
			if contact_form.is_valid():
				first_name = contact_form.cleaned_data['first_name']
				last_name = contact_form.cleaned_data['last_name']
				address = contact_form.cleaned_data['address']
				zipcode = contact_form.cleaned_data['zipcode']
				phone = contact_form.cleaned_data['phone']
				sender = contact_form.cleaned_data['email']
				subject = contact_form.cleaned_data['subject']
				subject = subject + '-' + first_name + ' ' + last_name
				message = contact_form.cleaned_data['message']
				recipients = [site_settings_processor(request)['site_email'],]
				fullemail = first_name + " " + last_name + " " + "<" + sender + ">"
				send_mail(subject, message, fullemail, recipients, fail_silently=False)
				context_dictionary['first_name'] = contact_form.cleaned_data['first_name']
			else:
				context_dictionary['form_errors'], context_dictionary['contact_form'] = True, contact_form
		else:
			pass
	else:
		contact_form = ContactForm()
		context_dictionary['contact_form'] = contact_form
