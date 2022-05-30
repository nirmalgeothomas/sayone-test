from django.conf.urls import url
from scmapp import views

app_name = 'scmapp'

urlpatterns = [
    url(r'^registration', views.index),
    url(r'^user_home', views.user_home),
    url(r'^test', views.test, name='test'),
    url(r'^login_user', views.login_user, name='login_user'),


    url(r'^rphome', views.rphome, name='rphome'),
    url(r'^success', views.success, name='success'),
    url(r'^rpbase', views.rpbase, name='rpbase'),
    url(r'^base', views.base, name='base'),
    url(r'^base2', views.base2, name='base2'),
    url(r'^tablepagination', views.tablepagination, name='tablepagination'),
    url(r'^admintablepagination', views.admintablepagination,
        name='admintablepagination'),

    url(r'^admin_login', views.admin_login, name='admin_login'),
    url(r'^login_admin', views.login_admin, name='login_admin'),

    url(r'^admin_home', views.admin_home, name='admin_home'),
    url(r'^user_home', views.user_home, name='user_home'),

    url(r'^user_event', views.user_event, name='user_event'),
    url(r'^ground_booking', views.ground_booking, name='ground_booking'),
    url(r'^db_ground_booking', views.db_ground_booking, name='db_ground_booking'),

    url(r'^admin_booking', views.admin_booking, name='admin_booking'),
    url(r'^admin_event', views.admin_event, name='admin_event'),

    url(r'^update_event/(?P<id>\d+)/$', views.update_event, name='update_event'),
    url(r'^db_update_event/(?P<id>\d+)/$',
        views.db_update_event, name='db_update_event'),
    url(r'^db_delete_event/(?P<id>\d+)/$',
        views.db_delete_event, name='db_delete_event'),

    url(r'^add_event', views.add_event, name='add_event'),
    url(r'^db_add_event', views.db_add_event, name='db_add_event'),

    url(r'^user_logout', views.user_logout, name='user_logout'),
    url(r'^admin_logout', views.admin_logout, name='admin_logout'),
]
