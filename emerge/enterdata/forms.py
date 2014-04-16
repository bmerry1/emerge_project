from django import forms
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory
from enterdata.models import Participant, Address, Phone


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'password')

PREFIX_CHOICES = (
		('Mr.', 'Mr.'),
		('Mrs.', 'Mrs.'),
		('Miss', 'Miss'),
		('Ms.', 'Ms.'),
		('Dr.', 'Dr.'),
	)

GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female'),
)

RACE_CHOICES = (
	('African American', 'African American'),
	('Caucasian', 'Caucasian'),
	('Hispanic', 'Hispanic'),
	('Other', 'Other'),
)
class ParticipantsForm(forms.ModelForm):
	participant_prefix = forms.ChoiceField(choices=PREFIX_CHOICES, help_text="Prefix", required=False)
	participant_fname = forms.CharField(max_length=200, help_text="First Name")
	participant_lname = forms.CharField(max_length=200, help_text="Last Name")
	participant_suffix = forms.CharField(max_length=200, help_text="Suffix", required=False)
	participant_gender = forms.ChoiceField(choices=GENDER_CHOICES, help_text="Gender")
	participant_age = forms.IntegerField(help_text="Age")
	participant_race = forms.ChoiceField(choices=RACE_CHOICES, help_text="Race/Ethnicity")

	class Meta:
		model = Participant

class PhoneForm(forms.ModelForm):
	class Meta:
		model = Phone

# inlineformset_factory creates a Class from a parent model (Participant)
# to a child model (Address)
ParticpantAddressFormSet = inlineformset_factory(Participant, Address, extra=1)
ParticpantPhoneFormSet = inlineformset_factory(Participant, Phone)
