Link : https://www.hackerrank.com/challenges/30-sorting/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))    
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
                count += 1
    print(f'Array is sorted in {count} swaps.')
    print('First Element:', a[0])
    print('Last Element:', a[-1])
