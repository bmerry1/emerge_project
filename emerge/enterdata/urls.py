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

)