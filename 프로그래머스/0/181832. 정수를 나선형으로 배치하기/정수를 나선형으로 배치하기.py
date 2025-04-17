def solution(n):
    answer = [[0] * n for _ in range(n)]
    
    # 오른쪽, 아래, 왼쪽, 위
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    x,y = 0,0   # 시작 위치
    direction = 0   # 현재 방향 인덱스
    
    for num in range(1, n*n+1):
        answer[x][y] = num
        
        # 다음 위치 계산
        nx = x + dx[direction]
        ny = y + dy[direction]
        
        # 경계 검사, 이미 숫자가 채워져 있는지 확인
        if nx < 0 or nx >= n or ny < 0 or ny >= n or answer[nx][ny] != 0:
            direction = (direction + 1) % 4
            nx = x + dx[direction]
            ny = y + dy[direction]
        
        x,y = nx,ny
        
    return answer