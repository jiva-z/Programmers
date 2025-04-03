def solution(n, m, section):
    answer = 0
    last_painted = 0  # 마지막으로 칠한 구역
    
    for s in section:
        if s > last_painted:  # 아직 칠하지 않은 구역이면
            answer += 1  # 롤러 사용 횟수 증가
            last_painted = s + m - 1  # 현재 롤러로 칠할 수 있는 구역의 끝
        
        # 만약 마지막 구역을 넘어간다면, n으로 제한
        if last_painted > n:
            last_painted = n
        
            
    return answer