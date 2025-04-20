import heapq

def solution(n, works):
    answer = 0
    
    # 모든 작업량의 합이 n 이하: 피로도 0 
    if sum(works) <= n:
        return 0
    
    # 최대 힙 구현 (음수로 변환)
    heap = [-w for w in works]
    heapq.heapify(heap)

    
    for _ in range(n):
        max_work = heapq.heappop(heap)
        if max_work == 0:
            break
        heapq.heappush(heap,max_work + 1)   # 음수이므로 +1을 해야 일을 줄이는 것
    
    answer = sum(h**2 for h in heap)
    
    return answer