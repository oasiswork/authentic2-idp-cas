import datetime

from django.db.models import query
from django.utils.timezone import now

from model_utils import managers

from . import app_settings


class CasTicketQuerySet(query.QuerySet):
    def clean_expired(self):
        '''Remove expired tickets'''
        self.filter(expire__gte=now()).delete()

    def cleanup(self):
        '''Delete old tickets'''
        delta = datetime.timedelta(seconds=app_settings.TICKET_EXPIRATION)
        qs = self.filter(creation__lt=now()-delta)
        qs.delete()

CasTicketManager = managers.PassThroughManager.for_queryset_class(CasTicketQuerySet)
