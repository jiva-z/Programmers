def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)

def lcm(a, b):
    return int(a * b / gcd(a, b))


def solution(a, b):
    answer = [gcd(a,b), lcm(a,b)]

    return answer

