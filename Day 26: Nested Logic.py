Link : https://www.hackerrank.com/challenges/30-nested-logic/problem?isFullScreen=true

d1, m1, y1 = list(map(int, input().split())) 
d2, m2, y2 = list(map(int, input().split()))
fine = 0
if y1 > y2:
    fine = 10000
elif y1 == y2:
    if m1 > m2:
        fine = 500 * (m1 - m2)
    elif m1 <= m2 and d1 > d2:
        fine = 15 * (d1 - d2)
print(fine)
