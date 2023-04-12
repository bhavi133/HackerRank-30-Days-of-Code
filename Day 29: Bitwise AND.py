Link : https://www.hackerrank.com/challenges/30-bitwise-and/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys


def bitwiseAnd(N, K):
    # return (K-1 if ((K-1) | K) <= N else K-2)
    if ((K-1) | K) <= N:
        return K-1
    else:
        return K-2
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        count = int(first_multiple_input[0])
        lim = int(first_multiple_input[1])
        res = bitwiseAnd(count, lim)
        fptr.write(str(res) + '\n')
    fptr.close()
