#!/usr/bin/env python

import sha, time, Cookie, os

cookie = Cookie.SimpleCookie()
string_cookie = os.environ.get('HTTP_COOKIE')
if string_cookie:
    print 'Content-Type: text/html\n'
    print '<html><body>'
    print 'HEYYYYYYY</body></html>'
else:
    print 'Content-Type: text/html\n'
    print '<html><body>'
    print 'SORRRYYYYY</body></html>'
