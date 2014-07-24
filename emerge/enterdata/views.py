from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView
from enterdata.forms import ParticipantsForm, ParticpantAddressFormSet, PhoneForm, ParticpantPhoneFormSet, EmergencyForm, FamilyForm, ProbationForm, LegalForm, LiteracyForm, KhanForm, OrientForm, VoskillsForm, WstatusForm, HoursForm, ProgramForm, CrewForm, SalaryForm
from enterdata.models import Participant, Address, Phone, Emergency, Family, Probation, Legal, Literacy_numeracy, Khan, Orientation, Voskills, Work_status, Hours, Program_enrollment, Crew_status, Salary
from django.template.defaultfilters import linebreaksbr
from django.core.context_processors import csrf


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

	context = RequestContext(request)
	context_dict = {'participants_id': participants_id}

	try:
		participant = Participant.objects.get(id=participants_id)
		context_dict['participant'] = participant

		addresses = Address.objects.filter(participant=participant)
		context_dict['addresses'] = addresses

		phone = Phone.objects.filter(participant=participant)
		context_dict['phone'] = phone

		emergency = Emergency.objects.filter(participant=participant)
		context_dict['emergency'] = emergency

		family = Family.objects.filter(participant=participant)
		context_dict['family'] = family

		probation = Probation.objects.filter(participant=participant)
		context_dict['probation'] = probation

		legal = Legal.objects.filter(participant=participant)
		context_dict['legal'] = legal

		literacy = Literacy_numeracy.objects.filter(participant=participant)
		context_dict['literacy'] = literacy

		khan = Khan.objects.filter(participant=participant)
		context_dict['khan'] = khan

		orient = Orientation.objects.filter(participant=participant)
		context_dict['orient'] = orient

		voskills = Voskills.objects.filter(participant=participant)
		context_dict['voskills'] = voskills

		wstatus = Work_status.objects.filter(participant=participant)
		context_dict['wstatus'] = wstatus

		hours = Hours.objects.filter(participant=participant)
		context_dict['hours'] = hours

		program = Program_enrollment.objects.filter(participant=participant)
		context_dict['program'] = program

		crew = Crew_status.objects.filter(participant=participant)
		context_dict['crew'] = crew

		salary = Salary.objects.filter(participant=participant)
		context_dict['salary'] = salary


	except Participant.DoesNotExist:
		pass

	if request.method == 'POST':
		query = request.POST.get('query')
		if query:
			query = query.strip()
			result_list = run_query(query)
			context_dict['result_list'] = result_list

	return render_to_response('enterdata/participant.html', context_dict, context)

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


def add_phone(request, participants_id):
	p = Participant.objects.get(id=participants_id)

	if request.method == "POST":
		f = PhoneForm(request.POST)
		if f.is_valid():
			c = f.save(commit=False)
			c.participant = p
			c.save()

			return HttpResponseRedirect('/emerge/participant/%s' % participants_id)	

	else:
		f = PhoneForm()

		args = {}
		args.update(csrf(request))

		args['participant'] = p
		args['form'] = f

		return render_to_response('enterdata/add_phone.html', args)


def add_emergency(request, participants_id):
	p = Participant.objects.get(id=participants_id)

	if request.method == "POST":
		f = EmergencyForm(request.POST)
		if f.is_valid():
			c = f.save(commit=False)
			c.participant = p
			c.save()

			return HttpResponseRedirect('/emerge/participant/%s' % participants_id)	

	else:
		f = EmergencyForm()

		args = {}
		args.update(csrf(request))

		args['participant'] = p
		args['form'] = f

		return render_to_response('enterdata/add_emergency.html', args)

def add_family(request, participants_id):
	p = Participant.objects.get(id=participants_id)

	if request.method == "POST":
		f = FamilyForm(request.POST)
		if f.is_valid():
			c = f.save(commit=False)
			c.participant = p
			c.save()

			return HttpResponseRedirect('/emerge/participant/%s' % participants_id)	

	else:
		f = FamilyForm()

		args = {}
		args.update(csrf(request))

		args['participant'] = p
		args['form'] = f

		return render_to_response('enterdata/add_family.html', args)

def add_probation(request, participants_id):
	p = Participant.objects.get(id=participants_id)

	if request.method == "POST":
		f = ProbationForm(request.POST)
		if f.is_valid():
			c = f.save(commit=False)
			c.participant = p
			c.save()

			return HttpResponseRedirect('/emerge/participant/%s' % participants_id)	

	else:
		f = ProbationForm()

		args = {}
		args.update(csrf(request))

		args['participant'] = p
		args['form'] = f

		return render_to_response('enterdata/add_probation.html', args)


def add_legal(request, participants_id):
	p = Participant.objects.get(id=participants_id)

	if request.method == "POST":
		f = LegalForm(request.POST)		#change form name
		if f.is_valid():
			c = f.save(commit=False)
			c.participant = p
			c.save()

			return HttpResponseRedirect('/emerge/participant/%s' % participants_id)	

	else:
		f = LegalForm()					#change form name

		args = {}
		args.update(csrf(request))

		args['participant'] = p
		args['form'] = f

		return render_to_response('enterdata/add_legal.html', args)

def add_lit(request, participants_id):
	p = Participant.objects.get(id=participants_id)

	if request.method == "POST":
		f = LiteracyForm(request.POST)		#change form name
		if f.is_valid():
			c = f.save(commit=False)
			c.participant = p
			c.save()

			return HttpResponseRedirect('/emerge/participant/%s' % participants_id)	

	else:
		f = LiteracyForm()					#change form name

		args = {}
		args.update(csrf(request))

		args['participant'] = p
		args['form'] = f

		return render_to_response('enterdata/add_lit.html', args)

def add_khan(request, participants_id):
	p = Participant.objects.get(id=participants_id)

	if request.method == "POST":
		f = KhanForm(request.POST)		#change form name
		if f.is_valid():
			c = f.save(commit=False)
			c.participant = p
			c.save()

			return HttpResponseRedirect('/emerge/participant/%s' % participants_id)	

	else:
		f = KhanForm()					#change form name

		args = {}
		args.update(csrf(request))

		args['participant'] = p
		args['form'] = f

		return render_to_response('enterdata/add_khan.html', args)

def add_orient(request, participants_id):
	p = Participant.objects.get(id=participants_id)

	if request.method == "POST":
		f = OrientForm(request.POST)		#change form name
		if f.is_valid():
			c = f.save(commit=False)
			c.participant = p
			c.save()

			return HttpResponseRedirect('/emerge/participant/%s' % participants_id)	

	else:
		f = OrientForm()					#change form name

		args = {}
		args.update(csrf(request))

		args['participant'] = p
		args['form'] = f

		return render_to_response('enterdata/add_orient.html', args)

def add_voskills(request, participants_id):
	p = Participant.objects.get(id=participants_id)

	if request.method == "POST":
		f = VoskillsForm(request.POST)		#change form name
		if f.is_valid():
			c = f.save(commit=False)
			c.participant = p
			c.save()

			return HttpResponseRedirect('/emerge/participant/%s' % participants_id)	

	else:
		f = VoskillsForm()					#change form name

		args = {}
		args.update(csrf(request))

		args['participant'] = p
		args['form'] = f

		return render_to_response('enterdata/add_voskills.html', args)

def add_wstatus(request, participants_id):
	p = Participant.objects.get(id=participants_id)

	if request.method == "POST":
		f = WstatusForm(request.POST)		#change form name
		if f.is_valid():
			c = f.save(commit=False)
			c.participant = p
			c.save()

			return HttpResponseRedirect('/emerge/participant/%s' % participants_id)	

	else:
		f = WstatusForm()					#change form name

		args = {}
		args.update(csrf(request))

		args['participant'] = p
		args['form'] = f

		return render_to_response('enterdata/add_wstatus.html', args)

def add_hours(request, participants_id):
	p = Participant.objects.get(id=participants_id)

	if request.method == "POST":
		f = HoursForm(request.POST)		#change form name
		if f.is_valid():
			c = f.save(commit=False)
			c.participant = p
			c.save()

			return HttpResponseRedirect('/emerge/participant/%s' % participants_id)	

	else:
		f = HoursForm()					#change form name

		args = {}
		args.update(csrf(request))

		args['participant'] = p
		args['form'] = f

		return render_to_response('enterdata/add_hours.html', args)

def add_program(request, participants_id):
	p = Participant.objects.get(id=participants_id)

	if request.method == "POST":
		f = ProgramForm(request.POST)		#change form name
		if f.is_valid():
			c = f.save(commit=False)
			c.participant = p
			c.save()

			return HttpResponseRedirect('/emerge/participant/%s' % participants_id)	

	else:
		f = ProgramForm()					#change form name

		args = {}
		args.update(csrf(request))

		args['participant'] = p
		args['form'] = f

		return render_to_response('enterdata/add_program.html', args)

def add_crew(request, participants_id):
	p = Participant.objects.get(id=participants_id)

	if request.method == "POST":
		f = CrewForm(request.POST)		#change form name
		if f.is_valid():
			c = f.save(commit=False)
			c.participant = p
			c.save()

			return HttpResponseRedirect('/emerge/participant/%s' % participants_id)	

	else:
		f = CrewForm()					#change form name

		args = {}
		args.update(csrf(request))

		args['participant'] = p
		args['form'] = f

		return render_to_response('enterdata/add_crew.html', args)

def add_salary(request, participants_id):
	p = Participant.objects.get(id=participants_id)

	if request.method == "POST":
		f = SalaryForm(request.POST)		#change form name
		if f.is_valid():
			c = f.save(commit=False)
			c.participant = p
			c.save()

			return HttpResponseRedirect('/emerge/participant/%s' % participants_id)	

	else:
		f = SalaryForm()					#change form name

		args = {}
		args.update(csrf(request))

		args['participant'] = p
		args['form'] = f

		return render_to_response('enterdata/add_salary.html', args)




#def submit_address(request):
#	if request.POST:

#		form = 