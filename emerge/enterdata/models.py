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
	address_program = models.CharField(max_length=200)
	address_ln1 = models.CharField(max_length=200)
	address_ln2 = models.CharField(max_length=200)
	address_city = models.CharField(max_length=200)
	address_state = models.CharField(max_length=2)
	address_zipcode = models.IntegerField(max_length=5)
	address_moveindate = models.DateField()

	class Meta:
		unique_together = ('participant', 'address_moveindate',)

	def __unicode__(self):
		return ' '.join ([
			self.address_city,
			self.address_state,
		])


