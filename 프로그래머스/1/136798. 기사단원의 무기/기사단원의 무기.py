def solution(number, limit, power):
    answer = 0
    number_list = []
    
    for i in range(1, number + 1):
        number_count = 0
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                if j * j == i:  # 제곱근인 경우
                    number_count += 1
                else:
                    number_count += 2  # 대응되는 쌍이 있는 경우
        
        if number_count > limit:
            number_count = power
        
        answer += number_count
    
    return answer
