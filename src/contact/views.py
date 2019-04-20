from django.shortcuts import render
from django.views.generic.edit import CreateView, FormView
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

class ContactView(FormView):
	form_class = ContactForm
	template_name = 'static_templates/contact.html'
	success_url = '/contact/'


	def form_valid (self, form):
		
		comment = form.cleaned_data['comment']
		name = form.cleaned_data['name']
		subject = 'Blood Bank Donation'
		message = '%s %s' %(comment, name)
		from_email = form.cleaned_data['email']

		send_mail (
			
			subject,
			message,
			from_email,
			[settings.EMAIL_HOST_USER],
			fail_silently=True,

			)
		return super(ContactView, self).form_valid(form)


	def get_context_data (self, *args, **kwargs):
		context = super(ContactView, self).get_context_data(*args, **kwargs)
		context['title'] = 'Contact'
		return context



