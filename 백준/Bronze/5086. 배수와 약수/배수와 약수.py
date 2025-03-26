while True:
    n, m = map(int, input().split()) # 공백으로 분리
    if n == 0 and m == 0:
        break
    # 만약 n이랑 m이 둘 다 0이면 멈춰!
    else: # 둘 다 0이 아니라면 계속 일단 할 거 해!
        if m % n == 0:
            print("factor") # 첫 번째 숫자(n)가 두 번째 숫자(m)의 약수인 경우
        elif n % m == 0:
            print("multiple") # n으로 m을 나눴을 때 나머지가 0이라면?
        else:
            print("neither")