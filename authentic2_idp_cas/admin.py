from django.contrib import admin
from models import *

class CasServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'domain')

class CasTicketAdmin(admin.ModelAdmin):
    list_display = ('user', 'service', 'ticket_id', 'valid', 'expire')

admin.site.register(CasService, CasServiceAdmin)
admin.site.register(CasTicket, CasTicketAdmin)
