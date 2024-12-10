def solution(numbers):
    list = [0,1,2,3,4,5,6,7,8,9]
    
    for i in range(len(numbers)):
        if numbers[i] in list:
            list.remove(numbers[i])
    
    return sum(list)