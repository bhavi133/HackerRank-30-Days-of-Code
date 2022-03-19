Link : https://www.hackerrank.com/challenges/30-review-loop/problem?isFullScreen=true

t = int(input())
lst = []
for i in range(t):
    words = input()
    str1 = ""
    str2 = ""
    for j in range(len(words)):
        if j % 2 == 0:
            str1 += words[j]
        else:
            str2 += words[j]
    lst.append(str1 + " " + str2)
    
for i in lst:
    print(i)
