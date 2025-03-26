import sys

T = int(sys.stdin.readline())
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    last_computer = pow(a, b, 10)  # 모듈러 연산 사용
    if last_computer == 0:  # 10으로 나누면 나머지가 0이면 10번 컴퓨터
        print(10)
    else:
        print(last_computer)