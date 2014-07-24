from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Participant(models.Model):

	participant_prefix = models.CharField(max_length=200)
	participant_fname = models.CharField(max_length=200)
	participant_lname = models.CharField(max_length=200)
	participant_suffix = models.CharField(max_length=200)
	participant_gender = models.CharField(max_length=6)
	participant_age = models.IntegerField()
	participant_race = models.CharField(max_length=45)

	def __unicode__(self):
		return self.participant_fname

class UserProfile(models.Model):
	user_fname = models.CharField(max_length=200)
	user_lname = models.CharField(max_length=200)
	user_login = models.OneToOneField(User)
	user_email = models.EmailField(max_length=254, blank=True)

	def __unicode__(self):
		return self.user_login

class Address(models.Model):

	participant = models.ForeignKey(Participant)
	address_program = models.CharField(max_length=200, help_text="Program Name", blank=True)
	address_ln1 = models.CharField(max_length=200, help_text="Street Address", blank=True)
	address_ln2 = models.CharField(max_length=200, help_text="Apartment No.", blank=True)
	address_city = models.CharField(max_length=200, help_text="City")
	address_state = models.CharField(max_length=2, help_text="State")
	address_zipcode = models.CharField(max_length=5, help_text="Zipcode")
	address_moveindate = models.DateField(help_text="Date of Move In")

	class Meta:
		unique_together = ('participant', 'address_moveindate',)

	def __unicode__(self):
		return ' '.join ([
			self.address_city,
			self.address_state,
		])

class Phone(models.Model):

	participant = models.ForeignKey(Participant)
	phone_type = models.CharField(max_length=200, help_text="Phone Type")
	phone_number = models.CharField(max_length=10, help_text="Phone Number")
	

	def __unicode__(self):
		return self.phone_number


class Emergency(models.Model):

	participant = models.ForeignKey(Participant)
	emergency_fname = models.CharField(max_length=200)
	emergency_lname = models.CharField(max_length=200)
	emergency_phone = models.CharField(max_length=10)

	def __unicode__(self):
		return self.emergency_phone

class Family(models.Model):

	participant = models.ForeignKey(Participant)
	family_residence = models.CharField(max_length=200, help_text="Residence Type")
	family_children = models.CharField(max_length=20, help_text="Number of Children")

	def __unicode__(self):
		return self.family_residence

class Probation(models.Model):

	participant = models.ForeignKey(Participant)
	probation_name = models.CharField(max_length=200, help_text="Officer Name")
	probation_phone = models.CharField(max_length=10, help_text="Probation Contact Phone")
	probation_end_dt = models.DateField(help_text="Date of End of Probation")

	def __unicode__(self):
		return self.probation_name

class Legal(models.Model):

	participant = models.ForeignKey(Participant)
	legal_charges = models.CharField(max_length=200, help_text="Charges")
	legal_convict_dt = models.DateField(help_text="Date of Conviction")
	legal_time_incar = models.CharField(max_length=200, help_text="Time Incarcerated") 
	legal_supervisor = models.CharField(max_length=200, help_text="Supervisor Name", blank=True)


	def __unicode__(self):
		return self.legal_charges

class Literacy_numeracy(models.Model):

	participant = models.ForeignKey(Participant)
	litnum_timepoint = models.CharField(max_length=200, help_text="Timepoint")
	litnum_type = models.CharField(max_length=200, help_text="Type of Assessment")
	litnum_dt = models.DateField(help_text="Date of Assessment") 
	litnum_raw = models.CharField(max_length=200, help_text="Raw Score", blank=True)
	litnum_casas = models.CharField(max_length=200, help_text="CASAS Scale Score", blank=True)

	def __unicode__(self):
		return self.litnum_timepoint

class Khan(models.Model):

	participant = models.ForeignKey(Participant)
	khan_dt = models.DateField(help_text="Date of Khan Tutorial")

	def __unicode__(self):
		return self.khan_dt

class Orientation(models.Model):

	participant = models.ForeignKey(Participant)
	orientation_group = models.CharField(max_length=200, help_text="Cohort Information")
	orientation_referral = models.CharField(max_length=200, help_text="Referral Source")
	orientation_supervision = models.CharField(max_length=200, help_text="Supervisor")
	orientation_startdt = models.DateField(help_text="Orientation Start Date")
	orientation_compdt = models.DateField(help_text="Date Completed Orientation")
	orientation_education_level = models.CharField(max_length=200, help_text="Education")
	orientation_medical_insurance = models.CharField(max_length=200, help_text="Insured")
	orientation_assessdt = models.DateField(help_text="Date Assessed")
	orientation_wksp_startdt = models.DateField(help_text="Workshop Start Date")
	orientation_wksp_enddt = models.DateField(help_text="Workshop End Date")
	orientation_wksp_complete = models.CharField(max_length=200, help_text="Workshop Completion Status")
	orientation_enrolleddt = models.DateField(help_text="Date of Program Enrollment")
	orientation_firstpayrolldt = models.DateField(help_text="First Day on EMERGE Payroll")
	
	def __unicode__(self):
		return self.orientation_startdt

class Voskills(models.Model):

	participant = models.ForeignKey(Participant)
	voskills_osha = models.CharField(max_length=200, help_text="OSHA Certified")
	voskills_osha_card = models.CharField(max_length=200, help_text="OSHA Card")
	voskills_ct_driver = models.CharField(max_length=200, help_text="CT Driver's License")
	voskills_primary = models.CharField(max_length=200, help_text="Primary Skill")
	voskills_service = models.CharField(max_length=200, help_text="Community Service")

	def __unicode__(self):
		return self.voskills_primary

class Work_status(models.Model):

	participant = models.ForeignKey(Participant)
	wstatus_start_dt = models.DateField(help_text="Program Work Start Date")
	wstatus_exit_dt = models.DateField(help_text="Program Work End Date", null=True, blank=True)
	wstatus_exit_status = models.CharField(max_length=200, help_text="How Referred Out of Program")
	wstatus_core_part = models.CharField(max_length=200, help_text="CORE Participation Status")
	wstatus_success = models.CharField(max_length=200, help_text="Participant Success")
	wstatus_notes = models.CharField(max_length=200, help_text="Related Notes")

	def __unicode__(self):
		return self.wstatus_start_dt

class Hours(models.Model):

	participant = models.ForeignKey(Participant)
	hours_activity = models.CharField(max_length=200, help_text="Activity Engaged In")
	hours_date = models.DateField(help_text="Date of Activity")
	hours_amt = models.CharField(max_length=200, help_text="Amount of Hours")

	def __unicode__(self):
		return self.hours_date

class Program_enrollment(models.Model):

	participant = models.ForeignKey(Participant)
	penroll_ssn = models.CharField(max_length=4, help_text="SSN - Last 4 Digits")
	penroll_complete = models.CharField(max_length=200, help_text="Complete Program")
	penroll_exit_dt = models.DateField(help_text="Program Exit Date", null=True, blank=True)
	penroll_exit_status = models.CharField(max_length=200, help_text="Program Exit Status", null=True, blank=True)

	def __unicode__(self):
		return self.penroll_ssn

class Crew_status(models.Model):

	participant = models.ForeignKey(Participant)
	crewstat_emply_type = models.CharField(max_length=200, help_text="Full or Part-time Work")
	crewstat_employer = models.CharField(max_length=200, help_text="Employer")
	crewstat_startdt = models.DateField(help_text="Work Start Date")
	crewstat_status = models.CharField(max_length=200, help_text="Notes on Participant Status")

	def __unicode__(self):
		return self.hours_date

class Salary(models.Model):

	participant = models.ForeignKey(Participant)
	salary_date = models.DateField(help_text="Date Salary Recorded")
	salary_amt = models.CharField(max_length=200, help_text="Salary")
	salary_scale = models.CharField(max_length=200, help_text="Salary Scale")

	def __unicode__(self):
		return self.salary_date

		
