#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""

import urllib.request
Url0 = "https://alx-intranet.hbtn.io/status"
req = urllib.request.Request(Url0)

with urllib.request.urlopen(req) as response:
    # Displaying information about the response body
    res = response.read()
    print("Body response:")
    print("    - type:", type(res))
    print("    - content:", res)
    print("    - utf8 content:", res.decode('utf-8'))
