a, b = map(int, input().split())
c = int(input())

time = a * 60 + b + c

hour = time // 60 % 24  # 24시간 처리
min = time % 60

print(hour, min)
