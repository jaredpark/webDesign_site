from django.conf.urls import patterns, url
# from user_interface.forms import MyProfileForm
from user_interface.models import MyProfileForm

from myProfiles import views

urlpatterns = patterns('',
  # url(r'^create/$',
    # views.create_profile,
    # name='profiles_create_profile'),
  # url(r'^edit/$',
  #   views.edit_profile,
  #   name='profiles_edit_profile'),
  url(r'^edit', 
    views.edit_profile, 
    {'form_class': MyProfileForm},
    name='profiles_edit_profile'),
  url(r'^home/$',
    views.profile_detail,
    name='profiles_profile_detail'),
  url(r'^(?P<username>\w+)/$',
    views.profile_detail,
    name='profiles_profile_detail'),
  # url(r'^$',
  #   views.profile_list,
  #   name='profiles_profile_list'),
)