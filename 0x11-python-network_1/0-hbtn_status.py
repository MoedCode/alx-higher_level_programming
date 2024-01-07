#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""

import urllib.request
Url0 = "https://alx-intranet.hbtn.io/status"
req = urllib.request.Request(Url0)

with urllib.request.urlopen(req) as res:
    # Displaying information about the response body
    print("Body response:")
    print("    - type:", type(res.read()))
    print("    - content:", res.read())
    print("    - utf8 content:", res.read().decode('utf-8'))
