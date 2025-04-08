def solution(numbers, n):
    answer = 0
    for number in numbers:
        if answer > n:
            return answer
        else:
            answer += number
        
    return answer