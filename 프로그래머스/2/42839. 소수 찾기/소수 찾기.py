from itertools import permutations

# 소수 판별 함수
def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2,int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    
def solution(numbers):
    prime_set = set()
    
    # 숫자 길이에 따라 조합 생성
    for r in range(1, len(numbers)+1):
        for perm in permutations(numbers, r):
            num = int(''.join(perm))
            
            if isPrime(num):
                prime_set.add(num)
    
    return len(prime_set)