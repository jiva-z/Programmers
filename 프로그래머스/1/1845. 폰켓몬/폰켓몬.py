def solution(nums):
    # set은 요소가 중복X, 순서없는 자료형
    answer = len(set(nums))
    
    if answer > len(nums)/2:
        return len(nums)/2
    return answer
    
    