
def solution(arr):
    # 함수를 완성하세요
    stack = []
    for s in arr:
        if len(stack) == 0 or stack[-1] != s:
            stack.append(s)

    return stack
