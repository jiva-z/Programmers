def solution(numbers):
    # 숫자를 문자열로 변환
    numbers = list(map(str, numbers))
    
    # 정렬 기준을 설정
    numbers.sort(key=lambda x: x*4, reverse=True)
    
    # 0으로만 구성된 경우
    if numbers[0] == '0':
        return '0'
    
    # 정렬된 숫자를 결합하여 결과 반환
    return ''.join(numbers)
