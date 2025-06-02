def solution(l, r):
    answer = []
    
    for i in range(l, r+1):
        if all(ch in '05' for ch in str(i)):
            answer.append(i)
    if not answer:
        return [-1]

    return answer