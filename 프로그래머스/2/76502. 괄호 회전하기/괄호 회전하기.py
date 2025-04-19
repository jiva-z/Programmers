def solution(s):
    answer = 0
    
    pair = {')': '(', ']': '[', '}': '{'}
    
    # 문자열 길이가 홀수면 바로 0 반환
    if len(s) % 2 != 0:
        return 0
    
    def is_valid(brackets):    
        stack = []
        for char in brackets:
            if char in pair.values():
                stack.append(char)
            else:
                # 스택이 비었거나 짝이 안 맞으면 실패
                if not stack or stack[-1] != pair[char]:
                    return False
                stack.pop()
        return not stack  # 스택이 비어있어야 올바름
    
    for x in range(len(s)):
        rotated = s[x:] + s[:x]
        if is_valid(rotated):
            answer += 1
            
    return answer
        