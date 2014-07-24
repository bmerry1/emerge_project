from django.conf.urls import patterns, include, url
from enterdata import views
import enterdata.views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^dashboard/$', views.dashboard, name='dashboard'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^add_participant/$', enterdata.views.ParticipantCreateView.as_view(), name='add_participant'),
	url(r'^all_participants/$', views.all_participants, name='all_participants'),
	url(r'^participant/(?P<participants_id>\d+)/$', views.participant, name='participant'),
	url(r'^add_phone/(?P<participants_id>\d+)/$', views.add_phone, name='add_phone'),
	url(r'^add_emergency/(?P<participants_id>\d+)/$', views.add_emergency, name='add_emergency'),
	url(r'^add_family/(?P<participants_id>\d+)/$', views.add_family, name='add_family'),
	url(r'^add_probation/(?P<participants_id>\d+)/$', views.add_probation, name='add_probation'),
	url(r'^add_legal/(?P<participants_id>\d+)/$', views.add_legal, name='add_legal'),
	url(r'^add_lit/(?P<participants_id>\d+)/$', views.add_lit, name='add_lit'),
	url(r'^add_khan/(?P<participants_id>\d+)/$', views.add_khan, name='add_khan'),
	url(r'^add_orient/(?P<participants_id>\d+)/$', views.add_orient, name='add_orient'),
	url(r'^add_voskills/(?P<participants_id>\d+)/$', views.add_voskills, name='add_voskills'),
	url(r'^add_wstatus/(?P<participants_id>\d+)/$', views.add_wstatus, name='add_wstatus'),
	url(r'^add_hours/(?P<participants_id>\d+)/$', views.add_hours, name='add_hours'),
	url(r'^add_program/(?P<participants_id>\d+)/$', views.add_program, name='add_program'),
	url(r'^add_crew/(?P<participants_id>\d+)/$', views.add_crew, name='add_crew'),
	url(r'^add_salary/(?P<participants_id>\d+)/$', views.add_salary, name='add_salary')


)