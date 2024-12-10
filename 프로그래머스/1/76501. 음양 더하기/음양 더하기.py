def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i] == True:
            answer += int(absolutes[i])
        else:
            answer -= int(absolutes[i]) 
    
    return answer