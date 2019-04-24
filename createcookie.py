#!/usr/bin/python3

import hashlib, time, os
from http import cookies

cookie = cookies.SimpleCookie()
string_cookie = os.environ.get('HTTP_COOKIE')

# If new session
if not string_cookie:
    # The sid will be a hash of the server time
    time_string=str(time.time())
    sid = hashlib.sha256(time_string.encode('utf-8')).hexdigest()
    # Set the sid in the cookie
    cookie['sid'] = sid
    # Will expire in a year
    cookie['sid']['expires'] = 1 * 1 * 1 * 1 * 10

print(cookie)
print('Content-type: text/html\n')
print('<html><head><meta http-equiv = "refresh" content = "1; url = /cgi-bin/checkcookie.py"/></head><body>')
print('</body></html>')
