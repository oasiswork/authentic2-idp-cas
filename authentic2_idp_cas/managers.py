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


class CasServiceQuerySet(query.QuerySet):
    def for_domain(self, domain):
        q = query.Q(domain=domain)
        parts = domain.split('.')
        for i in range(1, len(parts)):
            q |= query.Q(domain='.%s' % '.'.join(parts[i:]))
        return self.filter(q).order_by('-domain')

CasServiceManager = managers.PassThroughManager.for_queryset_class(CasServiceQuerySet)

CasTicketManager = managers.PassThroughManager.for_queryset_class(CasTicketQuerySet)
