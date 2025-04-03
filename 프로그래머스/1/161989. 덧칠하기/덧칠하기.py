def solution(n, m, section):
    answer = 0
    last_painted = 0
    
    for s in section:
        if s > last_painted:
            answer += 1
            last_painted = s + m - 1
        
         # 만약 마지막 구역을 넘어간다면, n으로 제한
        if last_painted > n:
            last_painted = n
        
            
    return answer