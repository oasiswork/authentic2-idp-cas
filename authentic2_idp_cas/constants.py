# Constants #
CAS_NAMESPACE    = 'http://www.yale.edu/tp/cas'
RENEW_PARAM      = 'renew'
SERVICE_PARAM    = 'service'
GATEWAY_PARAM    = 'gateway'
WARN_PARAM       = 'warn'
URL_PARAM        = 'url'
TICKET_PARAM     = 'ticket'
PGT_URL_PARAM    = 'pgtUrl'
PGT_PARAM        = 'pgt'
PGT_ID_PARAM     = 'pgtId'
PGT_IOU_PARAM    = 'pgtIou'
TARGET_SERVICE_PARAM = 'targetService'
USERNAME_FIELD   = 'username' # unused
PASSWORD_FIELD   = 'password' # unused
LT_FIELD         = 'lt'       # unused
SERVICE_TICKET_PREFIX = 'ST-'
ID_PARAM         = 'id'
CANCEL_PARAM     = 'cancel'

# ERROR codes
INVALID_REQUEST_ERROR  = 'INVALID_REQUEST'
INVALID_TICKET_ERROR   = 'INVALID_TICKET'
INVALID_SERVICE_ERROR  = 'INVALID_SERVICE'
INTERNAL_ERROR         = 'INTERNAL_ERROR'
BAD_PGT_ERROR          = 'BAD_PGT'

# XML Elements for CAS 2.0
SERVICE_RESPONSE_ELT       = 'serviceResponse'

AUTHENTICATION_SUCCESS_ELT = 'authenticationSuccess'
USER_ELT                   = 'user'
PGT_ELT                    = 'proxyGrantingTicket'
PROXIES_ELT                = 'proxies'
PROXY_ELT                  = 'proxy'

AUTHENTICATION_FAILURE_ELT = 'authenticationFailure'
CODE_ELT                   = 'code'

PROXY_SUCCESS_ELT          = 'proxySuccess'
PROXY_TICKET_ELT           = 'proxyTicket'

PROXY_FAILURE_ELT          = 'proxyFailure'

# XML Elements for CAS 3.0
ATTRIBUTES_ELT             = 'attributes'

# Templates

CAS10_VALIDATION_FAILURE = 'no\n\n'
CAS10_VALIDATION_SUCCESS = 'yes\n%s\n'
CAS20_VALIDATION_FAILURE = '''<cas:serviceResponse xmlns:cas='http://www.yale.edu/tp/cas'>
    <cas:authenticationFailure code="%s">
        %s
    </cas:authenticationFailure>
</cas:serviceResponse>'''
CAS20_VALIDATION_SUCCESS = '''<cas:serviceResponse xmlns:cas='http://www.yale.edu/tp/cas'>
    <cas:authenticationSuccess>
        <cas:user>%s</cas:user>
    </cas:authenticationSuccess>
</cas:serviceResponse>'''

SAML_RESPONSE_TEMPLATE = '''<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
<SOAP-ENV:Header/>
<SOAP-ENV:Body>
<Response xmlns="urn:oasis:names:tc:SAML:1.0:protocol" xmlns:saml="urn:oasis:names:tc:SAML:1.0:assertion" xmlns:samlp="urn:oasis:names:tc:SAML:1.0:protocol" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" IssueInstant="2013-05-16T16:07:35Z" MajorVersion="1" MinorVersion="1" Recipient="https://amonecole.monreseau.lan/webcalendar/login.php" ResponseID="{reponse_id}">
  <Status>
    <StatusCode Value="samlp:Success">
    </StatusCode>
  </Status>
  <Assertion xmlns="urn:oasis:names:tc:SAML:1.0:assertion" AssertionID="{assertion_id}" IssueInstant="{issue_instant}" Issuer="{issuer}" MajorVersion="1" MinorVersion="1">
<Conditions NotBefore="{not_before}" NotOnOrAfter="{not_on_or_after}">
      <AudienceRestrictionCondition>
        <Audience>{audience}</Audience>
      </AudienceRestrictionCondition>
    </Conditions>
    <AttributeStatement>
      <Subject>
        <NameIdentifier>{name_id}</NameIdentifier>
        <SubjectConfirmation>
          <ConfirmationMethod>urn:oasis:names:tc:SAML:1.0:cm:artifact</ConfirmationMethod>
        </SubjectConfirmation>
      </Subject>
      {attributes}

    </AttributeStatement>
    <AuthenticationStatement AuthenticationInstant="{authentication_instant}" AuthenticationMethod="{authentication_method}">
      <Subject>
        <NameIdentifier>{name_id}</NameIdentifier>
        <SubjectConfirmation>
          <ConfirmationMethod>urn:oasis:names:tc:SAML:1.0:cm:artifact</ConfirmationMethod>
        </SubjectConfirmation>
      </Subject>
    </AuthenticationStatement>
  </Assertion>
</Response>
</SOAP-ENV:Body>
</SOAP-ENV:Envelope>'''

