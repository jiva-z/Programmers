def solution(num_list):
    answer = 0
    odd = ''
    nodd = ''
    for i in num_list:
        if i % 2 != 0:
            odd += str(i)
        else:
            nodd += str(i)
            
    return int(nodd) + int(odd)