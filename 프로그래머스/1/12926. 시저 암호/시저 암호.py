def solution(s, n):
    answer = ''
    # 아스키 코드
    
    for alpha in s:
        if alpha == ' ':
            answer += ' '
        elif 'a' <= alpha <= 'z':
            answer += chr((ord(alpha) - ord('a') + n) % 26 + ord('a'))
        else:
            answer += chr((ord(alpha) - ord('A') + n) % 26 + ord('A'))
    
    
    return answer