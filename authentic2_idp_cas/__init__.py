from django.utils.timezone import now
from django.template.loader import render_to_string


class Plugin(object):
    def get_before_urls(self):
        from . import urls
        return urls.urlpatterns

    def get_apps(self):
        return [__name__]

    def logout_list(self, request):
        from . import models

        qs = models.CasService.objects.filter(accesstoken__user=request.user,
                accesstoken__expires__gt=now(), logout_url__isnull=False) \
                .distinct()

        l = []
        for client in qs:
            name = client.name
            url = client.get_logout_url()
            ctx = {
                'needs_iframe': client.logout_use_iframe,
                'name': name,
                'url': url,
                'iframe_timeout': client.logout_use_iframe_timeout,
            }
            content = render_to_string('idp/saml/logout_fragment.html', ctx)
            l.append(content)
        return l
