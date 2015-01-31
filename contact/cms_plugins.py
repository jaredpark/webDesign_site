from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _
from contact.forms import ContactForm, ExampleForm


class CMSContactPlugin(CMSPluginBase):
	name = "Contact Plugin"  # Name of the plugin
	render_template = "contact/contact_plugin.html"  # template to render the plugin with

	def render(self, context, instance, placeholder):
		request = context['request']
		context.update({
			'instance': instance,
			'placeholder': placeholder,
			'contact_form': ContactForm(),
			})
		return context

plugin_pool.register_plugin(CMSContactPlugin)  # register the plugin

class CMSExampleFormPlugin(CMSPluginBase):
	name = "Example Form Plugin"  # Name of the plugin
	render_template = "contact/example_form_plugin.html"  # template to render the plugin with

	def render(self, context, instance, placeholder):
		request = context['request']
		context.update({
			'instance': instance,
			'placeholder': placeholder,
			'example_form': ExampleForm(),
			})
		return context

plugin_pool.register_plugin(CMSExampleFormPlugin)  # register the plugin