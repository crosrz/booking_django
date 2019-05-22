from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse , HttpResponseRedirect
from .forms import ContactForm

def send_email(request):
	if request.method =='POST':
		form= ContactForm(request.POST)

		if form.is_valid():
			subject= form.cleaned_data('subject')
			from_email=form.cleaned_data('from_email')
			message=form.cleaned_data('message')

			try:
				send_mail(subject,message,from_email,['lear@exapmle.com'])


			except BadHeaderError:
				return HttpResponse('invalid email')

			return redirect('contact_us:send_success')



	else:
		form = ContactForm()


	context={ 
				'form': form
			}


	return render(request, 'contact_us/contact_us.html', context)


def send_success(request):
	return HttpResponse('Thanks for contacting us. We will get back to you soon.')

