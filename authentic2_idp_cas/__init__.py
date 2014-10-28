from django.template.loader import render_to_string

from . import utils

__version__ = '1.0'

class Plugin(object):
    def get_before_urls(self):
        from . import urls
        return urls.urlpatterns

    def get_apps(self):
        return [__name__]

    def logout_list(self, request):
        fragments = []
        for name, logout in utils.get_logout_urls(request):
            url = logout.get_logout_url()
            ctx = {
                'needs_iframe': logout.logout_use_iframe,
                'name': name,
                'url': url,
                'iframe_timeout': logout.logout_use_iframe_timeout,
            }
            content = render_to_string('authentic2_idp_cas/logout_fragment.html', ctx)
            fragments.append(content)
        return fragments
