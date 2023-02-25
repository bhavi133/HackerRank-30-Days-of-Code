Link : https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem?isFullScreen=true

from math import sqrt

n = int(input())
for i in range(n):
    x = int(input())
    if x == 1:
        print('Not prime')
    else:
        for i in range(2, int(sqrt(x)+1)):
            if x % i == 0:
                print('Not prime')
                break
        else:
            print('Prime')
