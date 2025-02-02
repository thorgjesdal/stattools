import requests
import pandas as pd
import re

url = 'https://tfrrs.org/athletes/8974696/Iowa/Abraham__Vogelsang_.html'
headers = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0'}
r =  requests.get(url, headers=headers)
#print(re.sub(r'width="\d+.%"' '', r.text))
t = pd.read_html(re.sub(r'width="\d+%"','', r.text))
print(t)
"""

fname = 'https___tfrrs.org_athletes_8974696_Iowa_Abraham__Vogelsang_.html'
with open(fname,'r') as f:
    t = pd.read_html(f)

print(t)
"""
