from xml.etree import ElementTree as ET


from django.test import TestCase
from django.test.client import RequestFactory, Client
from django.test.utils import override_settings


from authentic2.compat import get_user_model
from .models import CasTicket, CasService
from . import views
from . import constants


class CasTests(TestCase):
    LOGIN = 'test'
    PASSWORD = 'test'
    DOMAIN = 'casclient.com'
    SERVICE = 'https://%s/' % DOMAIN

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(self.LOGIN, password=self.PASSWORD)
        self.factory = RequestFactory()

    def test_cas_login_blacklist_failure(self):
        client = Client()
        response = client.get('/idp/cas/login/', {'service': self.SERVICE})
        self.assertEqual(response.status_code, 400)
        self.assertIn('is not allowed', response.content)

    @override_settings(A2_IDP_CAS_SERVICES=(SERVICE,))
    def test_cas_login_settings_whitelist(self):
        self.helper_test_cas_login()

    def test_cas_login_model_whitelist(self):
        CasService.objects.create(
                name=self.DOMAIN,
                slug=self.DOMAIN,
                domain=self.DOMAIN)
        self.helper_test_cas_login()

    def helper_test_cas_login(self):
        client = Client()
        response = client.get('/idp/cas/login/', {'service': self.SERVICE})
        self.assertIn('Location', response)
        self.assertTrue(response['Location'].startswith('http://testserver/login'))
        response = client.post(response['Location'], {
            'username': self.LOGIN, 
            'password': self.PASSWORD,
            'submit-password': ''})
        self.assertTrue(response['Location'].startswith('http://testserver/idp/cas/continue/'))
        response = client.get(response['Location'])
        self.assertTrue(response['Location'].startswith('https://casclient.com/?ticket=ST-'))
        # verify ticket
        ticket = response['Location'].split('ticket=')[1]
        response = client.get('/idp/cas/serviceValidate/', {'service': self.SERVICE, 'ticket': ticket})
        self.assertEqual(response.content, '''<?xml version='1.0' encoding='utf8'?>
<cas:serviceResponse xmlns:cas="http://www.yale.edu/tp/cas"><cas:authenticationSuccess><cas:user>test</cas:user></cas:authenticationSuccess></cas:serviceResponse>''')

    def test_service_validate_with_default_attributes(self):
        CasTicket.objects.create(
                ticket_id='ST-xxx',
                service='yyy',
                user=self.user,
                validity=True)
        request = self.factory.get('/idp/cas/serviceValidate',
                {'service': 'yyy', 'ticket': 'ST-xxx'})
        class TestCasProvider(views.CasProvider):
            def get_attributes(self, request, st):
                assert st.service == 'yyy'
                assert st.ticket_id == 'ST-xxx'
                return 'bob', { 'username': 'bob', 'email': 'bob@example.com' }
        provider = TestCasProvider()
        response = provider.service_validate(request)
        root = ET.fromstring(response.content)
        ns_ctx = { 'cas': constants.CAS_NAMESPACE }
        user_elt = root.find('cas:authenticationSuccess/cas:user', namespaces=ns_ctx)
        self.assertIsNotNone(user_elt)
        self.assertEqual(user_elt.text, 'bob')
        username_elt = root.find('cas:authenticationSuccess/cas:attributes/cas:username', namespaces=ns_ctx)
        self.assertEqual(username_elt.text, 'bob')
        email_elt = root.find('cas:authenticationSuccess/cas:attributes/cas:email', namespaces=ns_ctx)
        self.assertEqual(email_elt.text, 'bob@example.com')
