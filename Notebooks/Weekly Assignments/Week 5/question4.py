'''
This program takes a URL as a command-line argument and checks
whether there is a working website at that address.
It does this by requesting the URL and examining the HTTP
response status code.
'''

import sys
import urllib.request

if len(sys.argv) < 2:
    print("Error: No URL provided")
    sys.exit()

url = sys.argv[1]

try:
    response = urllib.request.urlopen(url)
    print("Website is working. HTTP status code:", response.status)
except Exception:
    print("Website is not reachable.")