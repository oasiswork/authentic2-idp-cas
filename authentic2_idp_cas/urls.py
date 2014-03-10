from django.conf.urls import patterns, include

from . import app_settings

urlpatterns = patterns('',
        ('^idp/cas/', include(app_settings.PROVIDER()().url)))
