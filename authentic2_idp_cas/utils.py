import random
import string
import urlparse
import urllib

ALPHABET = string.letters+string.digits+'-'

def get_logout_urls(request):
    '''Retrieve logout urls'''
    return ()

def make_id(prefix='', length=29):
    '''Generate CAS tickets identifiers'''
    l = length-len(prefix)
    content = ( random.SystemRandom().choice(ALPHABET) for x in range(l) )
    return prefix + ''.join(content)

def url_overwrite_parameters(url, **kwargs):
    splitted_url = urlparse.urlsplit(url)
    query = splitted_url.query
    parsed_query = urlparse.parse_qsl(query)
    parsed_query = [(a,b) for a, b in parsed_query if a not in kwargs]
    for a, b in kwargs.iteritems():
        parsed_query.append((a, unicode(b).encode('utf-8')))
    query = urllib.urlencode(parsed_query)
    splitted_url = splitted_url[:3] + (query,) + splitted_url[4:]
    return urlparse.urlunsplit(splitted_url)

def url_add_parameters(url, **kwargs):
    splitted_url = urlparse.urlsplit(url)
    query = splitted_url.query
    parsed_query = urlparse.parse_qsl(query)
    for a, b in kwargs.iteritems():
        parsed_query.append((a, unicode(b).encode('utf-8')))
    query = urllib.urlencode(parsed_query)
    splitted_url = splitted_url[:3] + (query,) + splitted_url[4:]
    return urlparse.urlunsplit(splitted_url)
