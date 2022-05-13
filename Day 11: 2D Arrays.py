Link : https://www.hackerrank.com/challenges/30-2d-arrays/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys


a = [*map(int,sys.stdin.read().split())]
print(max([sum([a[i+k] for k in (0,1,2,7,12,13,14)]) for i in range(0,22) if i%6 < 4])) 
