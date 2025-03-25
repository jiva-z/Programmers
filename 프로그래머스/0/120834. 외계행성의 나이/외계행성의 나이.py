def solution(age):
    answer = ''
    age_list = list(str(age))
    # a = 97
    # chr(): 아스키코드 -> 문자열, ord(): 문자열 -> 아스키코드
    for i in range(len(age_list)):
        answer += chr(int(age_list[i]) + 97)
            
    return answer