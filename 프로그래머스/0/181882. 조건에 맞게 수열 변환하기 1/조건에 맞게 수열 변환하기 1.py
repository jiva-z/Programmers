def solution(arr):
    answer = []
    for number in arr:
        if number >= 50 and number % 2 == 0:  # 50 이상의 짝수
            answer.append(number // 2)
        elif number < 50 and number % 2 != 0:  # 50 미만의 홀수
            answer.append(number * 2)
        else:  # 나머지 경우
            answer.append(number)
    
    return answer
