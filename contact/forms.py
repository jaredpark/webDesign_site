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

class ExampleForm(forms.Form):
	error_css_class = 'error'
	required_css_class = 'required'
	# a_line_of_text = forms.CharField(label='A text field, accepts a single line of text', required=True)
	# a_text_box = forms.CharField(label='A text area field, accepts multiple lines of text', max_length=400, initial='',
	# 	widget = forms.Textarea())
	true_or_false = forms.BooleanField(label="A logic field, allows selection of yes/no on/off", required=False, initial=True)
	a_choice = forms.ChoiceField(label='A choice field, allows selection one option from a list', choices=(('1', 'First Choice'), ('2', 'Second Choice'), ('3', 'Third Choice')))
	a_multiple_choice = forms.MultipleChoiceField(label='A multiple choice field, allows selection of one or more options from a list', choices=(('1', 'First Choice'), ('2', 'Second Choice'), ('3', 'Third Choice')),
		widget = forms.CheckboxSelectMultiple())
	an_image = forms.ImageField(label='An image field, provides image upload tool')
	an_email_address = forms.EmailField(label='An email field, accepts an email address', required=True)
	# a_web_address = forms.URLField(label='A URL field, accepts a web address', required=False, initial='http://www.example.com')
	# an_integer = forms.IntegerField(label='An integer field, accepts only integer numbers', required=False)
	# a_decimal = forms.DecimalField(label='A decimal field, accepts an integer or decimal number', required=False)
