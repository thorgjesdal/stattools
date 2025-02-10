import requests
import pandas as pd
import re
import io

url = 'https://tfrrs.org/athletes/8974696/Iowa/Abraham__Vogelsang_.html'
headers = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0'}
r =  requests.get(url, headers=headers)
f = io.StringIO(re.sub(r'[width,colspan]="\d+%"','', r.text))
t = pd.read_html(f)
print(type(t), len(t))
print(t[0])
print('X')
print(t[1], t[2])
print('XX')
print(t[3], t[4], t[5])
"""

fname = 'https___tfrrs.org_athletes_8974696_Iowa_Abraham__Vogelsang_.html'
with open(fname,'r') as f:
    t = pd.read_html(f)

print(t)
"""
