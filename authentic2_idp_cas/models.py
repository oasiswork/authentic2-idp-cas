from datetime import timedelta

from django.db import models
from django.utils.translation import ugettext_lazy as _

from authentic2.models import LogoutUrlAbstract

from . import app_setting, managers


class CasTicket(models.Model):
    '''Session ticket with a CAS 1.0 or 2.0 consumer'''

    ticket_id  = models.CharField(max_length=64)
    renew   = models.BooleanField(default=False)
    validity   = models.BooleanField(default=False)
    service = models.CharField(max_length=256)
    user    = models.CharField(max_length=128,blank=True,null=True)
    creation = models.DateTimeField(auto_now_add=True)
    '''Duration length for the ticket as seconds'''
    expire = models.DateTimeField(blank=True, null=True)

    objects = managers.CasTicketManager()

    def valid(self):
        return self.validity and not self.expired()

    def expired(self):
        '''Check if the given CAS ticket has expired'''
        if self.expire:
            return now() >= self.expire
        else:
            return False

class CasService(LogoutUrlAbstract):
    name = models.CharField(max_length=128, unique=True, verbose_name=_('name'))
    slug = models.SlugField(max_length=128, unique=True, verbose_name=_('slug'))
    domain = models.CharField(max_length=128, unique=True,
            verbose_name=_('domain'))

    class Meta:

