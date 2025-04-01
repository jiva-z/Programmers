def solution(n_str):
    answer = ''
    index = 0
    
    for i in range(len(n_str)):
        if n_str[i] != '0':
            index = i
            break
    
    answer += n_str[index:]    
    return answer