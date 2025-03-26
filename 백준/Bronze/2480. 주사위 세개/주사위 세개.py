answer = 0
a, b, c = map(int,input().split())

if a == b and b == c :
    answer = 10000 + a * 1000
elif a == b or b == c or a == c:
    if a == b or a == c:
        answer = 1000 + a * 100
    else:
        answer = 1000 + b * 100
else:
    answer = max(a,b,c) * 100

print(answer)