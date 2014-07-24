from django import forms
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory
from enterdata.models import Participant, Address, Phone, Emergency, Family, Probation, Legal, Literacy_numeracy, Khan, Orientation, Voskills, Work_status, Hours, Program_enrollment, Crew_status, Salary


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

RES_CHOICES = (
	('Live with Family', 'Live with Family'),
	('On Own', 'On Own'),
	('Corrections', 'Corrections'),
	('Homeless', 'Homeless'),
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
		fields = ('phone_type', 'phone_number')

class EmergencyForm(forms.ModelForm):
	emergency_fname = forms.CharField(max_length=200, help_text="First Name")
	emergency_lname = forms.CharField(max_length=200, help_text="Last Name")
	emergency_phone = forms.CharField(max_length=10, help_text="Phone Number")

	class Meta:
		model = Emergency
		fields = ('emergency_fname', 'emergency_lname', 'emergency_phone')

class FamilyForm(forms.ModelForm):
	family_residence = forms.ChoiceField(choices=RES_CHOICES, help_text="Residence Type", required=False)

	class Meta:
		model = Family
		fields = ('family_residence', 'family_children')

class ProbationForm(forms.ModelForm):

	class Meta:
		model = Probation
		fields = ('probation_name', 'probation_phone', 'probation_end_dt')

class LegalForm(forms.ModelForm):

	class Meta:
		model = Legal
		fields = ('legal_charges', 'legal_convict_dt', 'legal_time_incar', 'legal_supervisor')

class LiteracyForm(forms.ModelForm):

	class Meta:
		model = Literacy_numeracy
		fields = ('litnum_timepoint', 'litnum_type', 'litnum_dt', 'litnum_raw', 'litnum_casas')

class KhanForm(forms.ModelForm):

	class Meta:
		model = Khan
		fields = ('khan_dt',)

class OrientForm(forms.ModelForm):

	class Meta:
		model = Orientation
		fields = ('orientation_group', 'orientation_referral', 'orientation_supervision', 'orientation_startdt', 'orientation_compdt', 'orientation_education_level', 'orientation_medical_insurance', 'orientation_assessdt', 'orientation_wksp_startdt', 'orientation_wksp_enddt', 'orientation_wksp_complete', 'orientation_enrolleddt', 'orientation_firstpayrolldt')


class VoskillsForm(forms.ModelForm):

	class Meta:
		model = Voskills
		fields = ('voskills_osha', 'voskills_osha_card', 'voskills_ct_driver', 'voskills_primary', 'voskills_service')

class WstatusForm(forms.ModelForm):
	wstatus_exit_dt = forms.DateField(help_text="Program Work End Date", required=False)

	class Meta:
		model = Work_status
		fields = ('wstatus_start_dt', 'wstatus_exit_dt', 'wstatus_exit_status', 'wstatus_core_part', 'wstatus_success', 'wstatus_notes')

class HoursForm(forms.ModelForm):

	class Meta:
		model = Hours
		fields = ('hours_activity', 'hours_date', 'hours_amt')

class ProgramForm(forms.ModelForm):

	class Meta:
		model = Program_enrollment
		fields = ('penroll_ssn', 'penroll_complete', 'penroll_exit_dt', 'penroll_exit_status')

class CrewForm(forms.ModelForm):

	class Meta:
		model = Crew_status
		fields = ('crewstat_emply_type', 'crewstat_employer', 'crewstat_startdt', 'crewstat_status')

class SalaryForm(forms.ModelForm):

	class Meta:
		model = Salary
		fields = ('salary_date', 'salary_amt', 'salary_scale')




# inlineformset_factory creates a Class from a parent model (Participant)
# to a child model (Address)
ParticpantAddressFormSet = inlineformset_factory(Participant, Address, extra=1)
ParticpantPhoneFormSet = inlineformset_factory(Participant, Phone)
