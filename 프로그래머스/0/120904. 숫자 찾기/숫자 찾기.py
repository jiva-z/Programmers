def solution(num, k):
    answer = 0
    num_list = list(str(num))

    for i in range(len(num_list)):
        if k == int(num_list[i]):
            answer = i + 1
            break
        else:
            answer = -1
    
    return answer