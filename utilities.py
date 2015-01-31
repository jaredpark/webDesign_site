from context_processors import site_settings_processor
from django.core.mail import send_mail
from contact.forms import ContactForm, ExampleForm

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

def ExampleFormProcessor(request, context_dictionary):
	if request.method == 'POST':
		if 'example' in request.POST:
			# create a form instance and populate it with data from the request:
			example_form = ExampleForm(data=request.POST, files=request.FILES)
			# check whether it's valid:
			if example_form.is_valid():
				pass
			else:
				context_dictionary['form_errors'], context_dictionary['example_form'] = True, example_form
		else:
			pass
	else:
		example_form = ExampleForm()
		context_dictionary['example_form'] = example_form

from django.db.models import ImageField
from django.forms import forms
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _

class ContentTypeRestrictedImageField(ImageField):
	"""
	Same as ImageField, but you can specify:
	* content_types - list containing allowed content_types. Example: ['application/pdf', 'image/jpeg']
	* max_upload_size - a number indicating the maximum file size allowed for upload.
	2.5MB - 2621440
	5MB - 5242880
	10MB - 10485760
	20MB - 20971520
	50MB - 5242880
	100MB 104857600
	250MB - 214958080
	500MB - 429916160
	"""
	def __init__(self, *args, **kwargs):
		# self.content_types = kwargs.pop("content_types")
		self.max_upload_size = kwargs.pop("max_upload_size")
		super(ContentTypeRestrictedImageField, self).__init__(*args, **kwargs)
	def clean(self, *args, **kwargs):        
		data = super(ContentTypeRestrictedImageField, self).clean(*args, **kwargs)
		file = data.file
		try:
			# content_type = file.content_type
			# if content_type in self.content_types:
				if file._size > self.max_upload_size:
					raise forms.ValidationError(_('Please keep filesize under %s. Current filesize %s') % (filesizeformat(self.max_upload_size), filesizeformat(file._size)))
			# else:
				# raise forms.ValidationError(_('Filetype not supported.'))
		except AttributeError:
			pass        

		return data
