Link : https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem?isFullScreen=true

import sys

S = input().strip()

try: 
    print (int(S))
except ValueError: 
    print ("Bad String")
