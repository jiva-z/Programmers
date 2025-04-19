def solution(n, computers):
    visited = [False] * n  # 각 컴퓨터의 방문 여부를 저장하는 리스트
    count = 0  # 네트워크 개수를 카운트
    
    def dfs(node):
        visited[node] = True  # 현재 노드 방문 처리
        
        # 현재 노드와 연결된 모든 이웃 노드 확인
        for neighbor in range(n):
            # 자기 자신이 아니고, 연결되어 있으며, 아직 방문하지 않은 노드일 때
            if neighbor != node and computers[node][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)  # 해당 노드로 DFS 재귀 호출
                
    # 모든 컴퓨터를 순회하며 네트워크 탐색
    for i in range(n):
        if not visited[i]:  # 아직 방문하지 않은 컴퓨터 발견 시
            count += 1      # 새로운 네트워크 발견 → 카운트 증가
            dfs(i)          # 해당 컴퓨터부터 DFS 시작

    return count  # 총 네트워크 개수 반환
