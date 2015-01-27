from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
# from user_interface.forms import UserForm, UserProfileForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required
def account(request):
	# if '_auth_user_id' in request.session:
	# 	userId = request.session['_auth_user_id']
	# 	userDetails = user.objects.get(pk=userId)
	# user_profile = request.user.profile()
	# context_dictionary = { 'user_profile': user_profile, }
	context_dictionary = {}
	return(render(request, 'user_interface/account.html', context_dictionary))

# registration-redux obsoletes this code:

# def register(request):

# 	registered = False
# 	context_dictionary = { 'registered': registered, }

# 	if request.method == 'POST':
# 		user_form = UserForm(data=request.POST)
# 		profile_form = UserProfileForm(data=request.POST)
# 		if user_form.is_valid() and profile_form.is_valid():
# 			user = user_form.save()
# 			user.set_password(user.password)
# 			user.save()
# 			profile = profile_form.save(commit=False)
# 			profile.user = user
# 			profile.save()
# 			registered = True
# 			login_form = LoginForm()
# 			context_dictionary = {'user': user, 'login_form': login_form, 'registered': registered, }
# 			return(render(request, 'user_interface/register.html', context_dictionary ))
# 		else:
# 			context_dictionary= {'user_form': user_form, 'profile_form': profile_form, 'registered': registered, }
# 	else:
# 		user_form = UserForm()
# 		profile_form = UserProfileForm()
# 		context_dictionary= {'user_form': user_form, 'profile_form': profile_form, 'registered': registered, }
	
# 	return(render(request, 'user_interface/register.html', context_dictionary ))

# def myLogin(request):
# 	logged_in = False
# 	if request.method == 'POST':
# 		username = request.POST['username']
# 		password = request.POST['password']
# 		user = authenticate(username=username, password=password)
# 		if user:
# 			if user.is_active:
# 				login(request, user)
# 				logged_in = True
# 				return(HttpResponseRedirect('../accounts/account'))
# 			else:
# 				return(HttpResponse("Your account is not active. <a href='../contact/'>Contact Us</a> to reactivate your account."))
# 		else:
# 			login_form = LoginForm(request.POST)
# 			return(render(request, 'user_interface/login.html', {'login_form': login_form, 'login_errors': True, }))
# 	else:
# 		login_form = LoginForm()
# 		return(render(request, 'user_interface/login.html', {'login_form': login_form,}))

# @login_required
# def myLogout(request):
#     logout(request)
#     return(HttpResponseRedirect('/'))