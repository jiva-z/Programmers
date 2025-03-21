def solution(brown, yellow):
    answer = []
    yellow_x = 0    # yellow 가로길이
    yellow_y = 0    # yellow 세로길이
    
    for i in range(1, yellow+1):
        if yellow % i == 0:
            yellow_x = yellow // i
            yellow_y = i
            
            if 2 * yellow_x + 2 * yellow_y + 4 == brown:
                answer.append(yellow_x + 2)
                answer.append(yellow_y + 2)
                break
                
            # 가로 길이가 세로 길이와 같거나 세로 길이보다 길다고 했으므로 내림차순 정렬
            answer.sort(reverse = True) 
            
    return answer