#!/usr/bin/env python3

import hashlib, time, os
from http import cookies

cookie = cookies.SimpleCookie()
string_cookie = os.environ.get('HTTP_COOKIE')
if string_cookie:
    print('Content-Type: text/html\n')
    print('<html><body>')
    print('HEYYYYYYY</body></html>')
else:
    print('Content-Type: text/html\n')
    print('<html><body>')
    print('SORRRYYYYY</body></html>')
