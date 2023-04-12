Link : https://www.hackerrank.com/challenges/30-regex-patterns/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

arr = []

if __name__ == '__main__':
    N = int(input().strip())
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()
        firstName = first_multiple_input[0]
        emailID = first_multiple_input[1]
        # if re.compile("@gmail.com$").search(emailID):
        if re.search(".+@gmail\.com$", emailID):
            arr.append(firstName)
    arr.sort()
    for i in arr:
        print(i)
