from django import forms
from django.forms import ModelForm
from user_interface.models import UserProfile
from django.contrib.auth.models import User
from registration.forms import RegistrationForm

class MyRegistrationForm(RegistrationForm):
	first_name = forms.CharField(label='Your First Name')
	last_name = forms.CharField(label='Your Last Name')
	business_name = forms.CharField(label='Your Business Name (leave blank if none)', required=False)
	business_zipcode = forms.IntegerField(label='Business Zip Code (home if none)', required=True)

class MyProfileForm(ModelForm):
	# def __init__(self, *args, **kwargs):
	# 	super(MyProfileForm, self).__init__(*args, **kwargs)
	# 	try:
	# 		self.fields['email'].initial = self.instance.user.email
	# 		self.fields['first_name'].initial = self.instance.user.first_name
	# 		self.fields['last_name'].initial = self.instance.user.last_name
	# 	except User.DoesNotExist:
	# 		pass
 
	# email = forms.EmailField(label="Primary email",help_text='')
	# first_name = forms.CharField(label='First Name')
	# last_name = forms.CharField(label='Last Name')
 
	class Meta:
		model = UserProfile
		exclude = ('user', 'email', 'first_name', 'last_name', 'next_appointment', 'balance', 'public', 'dog')

	# def save(self, *args, **kwargs):
	# 	u = self.instance.user
	# 	u.email = self.cleaned_data['email']
	# 	u.first_name = self.cleaned_data['first_name']
	# 	u.last_name = self.cleaned_data['last_name']
	# 	u.save()
	# 	profile = super(MyProfileForm, self).save(*args,**kwargs)
	# 	return profile
	
# registration-redux obsoletes this code:

# class UserForm(forms.ModelForm):
# 	password = forms.CharField(widget=forms.PasswordInput())
# 	class Meta:
# 		model = User
# 		fields = ('username', 'password', 'email','first_name') #,'last_name')

# class UserProfileForm(forms.ModelForm):
# 	class Meta:
# 		model = UserProfile
# 		# exclude = ('user',)
# 		fields = ()

# class LoginForm(forms.Form):
# 	error_css_class = 'error'
# 	required_css_class = 'required'
# 	username = forms.CharField(label='Username', required=True)
# 	password = forms.CharField(label='Password', required=True, widget=forms.PasswordInput())