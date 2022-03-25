Link : https://www.hackerrank.com/challenges/30-binary-numbers/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
    binary  = bin(n).strip("0b")
    count = 0
    nums = []
    for i in str(binary):
        if i == "1":
            count += 1
        else:
            nums.append(count)
            count = 0
    nums.append(count)
    print(max(nums))
