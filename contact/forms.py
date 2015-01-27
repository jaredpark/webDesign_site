from django import forms

class ContactForm(forms.Form):
	error_css_class = 'error'
	required_css_class = 'required'
	first_name = forms.CharField(label='First Name', required=True)
	last_name = forms.CharField(label='Last Name', required=True)
	address = forms.CharField(label='Street Address', required=False)
	zipcode = forms.IntegerField(label='Zip Code', required=False)
	phone = forms.CharField(label='Phone Number', required=True)
	current_website = forms.URLField(label='Current Web Site', required=False, initial='http://www.example.com')
	email = forms.EmailField(label='Email Address', required=True)
	preferred_contact = forms.ChoiceField(label='Preferred contact', choices=(('phone', 'phone'), ('email', 'email')))
	availability = forms.MultipleChoiceField(label='When are you available?', choices=(('Evening', '4pm to 8pm'), ('Afternoon', 'noon to 4pm'), ('Morning', '8am to noon')),
		widget = forms.CheckboxSelectMultiple())
	permission = forms.BooleanField(label="Do you want to know the 3 common traits of successful websites?", required=False, initial=True)
	subject = forms.CharField(label='Subject', initial='Request a consultation')
	message = forms.CharField(label='Message', max_length=400, initial='Please provide any additional information about your project.',
		widget = forms.Textarea())