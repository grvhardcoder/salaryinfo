from django.conf.urls.defaults import *

from registration.forms import RegistrationFormUniqueEmail, RegistrationForm


urlpatterns = patterns('',


    url(
        r'^register/$', 
        "registration.views.register",
        {
        'form_class': RegistrationFormUniqueEmail,
        'backend': 'accounts.regbackend.RegBackend'
        },
        name='registration_register',
    ),

    url(
        r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 
        'django.contrib.auth.views.password_reset_confirm',
        name='auth_password_reset_confim',
    ),
    url(
        r'^reset/done/$', 
        'django.contrib.auth.views.password_reset_complete'
    ),
    url(
        r'^logout/$',
        'django.contrib.auth.views.logout', {'next_page': '/'},
        name='auth_logout',
    ),

    (r'', include('registration.backends.default.urls')),
)
