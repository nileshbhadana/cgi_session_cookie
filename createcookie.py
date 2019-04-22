#!/usr/bin/env python

import sha, time, Cookie, os

cookie = Cookie.SimpleCookie()
string_cookie = os.environ.get('HTTP_COOKIE')

# If new session
if not string_cookie:
    # The sid will be a hash of the server time
    sid = sha.new(repr(time.time())).hexdigest()
    # Set the sid in the cookie
    cookie['sid'] = sid
    # Will expire in a year
    cookie['sid']['expires'] = 1 * 1 * 1 * 1 * 10

print cookie
print 'Content-Type: text/html\n'
print '<html><head><meta http-equiv = "refresh" content = "1; url = /cgi-bin/checkcookie.py" /></head><body>'
print '</body></html>'
