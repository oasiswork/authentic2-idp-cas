class AppSettings(object):
    __DEFAULTS = {
            'SERVICES': (),
    }

    def __init__(self, prefix):
        self.prefix = prefix

    @property
    def PROVIDER(self):
        from django.utils.importlib import import_module
        cas_provider = self._setting('CAS_PROVIDER', 'authentic2_idp_cas.views.Authentic2CasProvider')
        module, cls = cas_provider.rsplit('.', 1)
        module = import_module(module)
        return getattr(module, cls)


    @property
    def TICKET_EXPIRATION(self):
        return self._setting('TICKET_EXPIRATION', 240)


    def _setting(self, name, dflt):
        from django.conf import settings
        return getattr(settings, self.prefix + name, dflt)


    def __getattr__(self, name):
        if name not in self.__DEFAULTS:
            raise AttributeError(name)
        return self._setting(name, self.__DEFAULTS[name])


# Ugly? Guido recommends this himself ...
# http://mail.python.org/pipermail/python-ideas/2012-May/014969.html
import sys
app_settings = AppSettings('A2_IDP_CAS_')
app_settings.__name__ = __name__
sys.modules[__name__] = app_settings
