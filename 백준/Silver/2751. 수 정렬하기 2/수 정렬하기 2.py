# N = int(input())
# number_list = []
# for i in range(N):
#     number_list.append(input()) 
# number_list.sort()
# print('\n'.join(number_list))

# 위 코드가 시간초과돼서 다른 방법 서칭

# sys.stdin.readline()사용 : \n 포함해서 인식 (input()은 \n 제거해야해서 시간 오래걸림)
import sys

n = int(input())
nums = []

for _ in range(n):
    nums.append(int(sys.stdin.readline()))

nums.sort()

for num in nums:
    print(num)