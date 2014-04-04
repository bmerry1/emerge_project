from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from enterdata.forms import ParticipantsForm
from enterdata.models import Participant


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

#def submit_address(request):
#	if request.POST:

#		form = 