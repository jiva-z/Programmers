def solution(k, m, score):
    answer = 0
    apple_list = []
    i = 0
    # score를 내림차순 정렬 후 m개 씩 끊어서 2차원 배열 apple_list에 저장
    score.sort(reverse=True)
    for i in range(0,len(score),i+m):
        apple_list.append(score[i:i+m])
        
    # 2차원 배열 apple_list 를 오름차순 정렬 후 맨 앞의 원소 * m 하여 answer에 더함
    apple_list.sort() # 2차원 배열 전체를 오름차순 정렬
    
    for i in range(len(apple_list)):
        apple_list[i].sort()  # 2차원 배열의 i번째 원소들이 담긴 배열 오름차순 정렬
        if len(apple_list[i]) == m:
            answer += apple_list[i][0] * m
    
    return answer