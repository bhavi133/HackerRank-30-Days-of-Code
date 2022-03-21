Link : https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem?isFullScreen=true

num = int(input())
lst = [input().split(' ') for i in range(num)]
dic = {k:v for k, v in lst}
while True:
    try:
        query = input()
        if query in dic:
            print(f"{query}={dic[query]}") 
        else:
            print("Not found")
    except:
        break
