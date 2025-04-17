def solution(myString):
    answer = ''
    
    for i, alpha in enumerate(myString):
        if alpha < 'l':
            answer += 'l'
        else:
            answer += alpha
    
    return answer