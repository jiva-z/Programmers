def solution(code):
    answer = ''
    mode = 0
    
    for idx, i in enumerate(code):
        if mode == 0 and code[idx] == '1':
            mode = 1
        elif mode == 0 and code[idx] != '1' and idx % 2 == 0:
            answer += code[idx]
        elif mode == 1 and code[idx] == '1':
            mode = 0
        elif mode == 1 and code[idx] != '1' and idx % 2 == 1:
            answer += code[idx]
    
    if not len(answer):
        answer = 'EMPTY'
    
    return answer