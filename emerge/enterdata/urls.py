from django.conf.urls import patterns, include, url
from enterdata import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^dashboard/$', views.dashboard, name='dashboard'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^add_participant/$', views.add_participant, name='add_participant'),
	url(r'^all_participants/$', views.all_participants, name='all_participants'),
	url(r'^participant/(?P<participants_id>\d+)/$', views.participant, name='participant'),

)