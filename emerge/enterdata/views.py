from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView
from enterdata.forms import ParticipantsForm, ParticpantAddressFormSet, PhoneForm, ParticpantPhoneFormSet
from enterdata.models import Participant, Phone


# Create your views here.
def index(request):
	context = RequestContext(request)

	context_dict = {'welcome': "Welcome to the EMERGE Data Portal.  If you have an account, please sign in now."}

	return render_to_response('enterdata/index.html', context_dict, context)

def user_login(request):
	context = RequestContext(request)
	context_dict = {}

	if request.method == 'POST':

		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)


		if user is not None:

			if user.is_active:

				login(request, user)
				return HttpResponseRedirect('/emerge/dashboard/')
			else:
				context_dict['disabled_account'] = True
				return render_to_response('enterdata/index.html', context_dict, context)
		else:
			print "Invalid login details: {0}, {1}".format(username, password)
			context_dict['bad_details'] = True
			return render_to_response('enterdata/index.html', context_dict, context)

	else:
		return render_to_response('enterdata/index.html', {}, context)


def user_logout(request):
	logout(request)

	return HttpResponseRedirect('/emerge/')

def dashboard(request):
	context = RequestContext(request)

	context_dict = {'dash': "You have now logged into the system.  Please review the dashboard information."}

	return render_to_response('enterdata/dashboard.html', context_dict, context)

def add_participant(request):
	context = RequestContext(request)

	if request.method == 'POST':
		form = ParticipantsForm(request.POST)

		if form.is_valid():
			form.save(commit=True)

			return dashboard(request)
		else:
			pass
	else:
		form = ParticipantsForm()

	return render_to_response('enterdata/add_participant.html', {'form': form}, context)

def all_participants(request):
	return render_to_response('enterdata/all_participants.html',
								{'all_participants': Participant.objects.all() })

def participant(request, participants_id=1):
	return render_to_response('enterdata/participant.html',
								{'participant': Participant.objects.get(id=participants_id) })

# CBV for creating inline forms
class ParticipantCreateView(CreateView):

	model = Participant
	template_name = 'enterdata/add_participant.html'
	form_class = ParticipantsForm
	success_url = '/emerge/all_participants/'

	def get(self, request, *args, **kwargs):

		#context = super(ParticipantCreateView, self).get_context_data(**kwargs)
		#if self.request.POST:
		#	context['formset'] = ParticpantAddressFormSet(self.request.POST)
		#else:
		#	context['formset'] = ParticpantAddressFormSet()
		#return context

		self.object = None
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		address_form = ParticpantAddressFormSet()

		# redirect to Participant view.
		return self.render_to_response(
			self.get_context_data(form=form, address_form=address_form))

	def post(self, request, *args, **kwargs):
		self.object = None
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		address_form = ParticpantAddressFormSet(self.request.POST)
		if (form.is_valid() and address_form.is_valid()):
			return self.form_valid(form, address_form)
		else:
			return self.form_invalid(form, address_form)

	def form_valid(self, form, address_form):
		#context = self.get_context_data()
		#formset = context['formset']
		#if formset.is_valid():
		#	self.object = form.save()
		#	formset.instance = self.object
		#	formset.save()
		#	return HttpResponseRedirect(self.get_success_url())

		#else:
		#	return self.render_to_response(
		#	self.get_context_data(form=form))

		self.object = form.save()
		address_form.instance = self.object
		address_form.save()
		return HttpResponseRedirect(self.get_success_url())

	def form_invalid(self, form, address_form):

		return self.render_to_response(
			self.get_context_data(form=form, address_form=address_form))

		

#def submit_address(request):
#	if request.POST:

#		form = 