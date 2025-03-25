def solution(my_string):
    answer = ''
    s = list(my_string.lower())
    s.sort()
    return ''.join(s)