def solution(citations):
    answer = 0
    
    n = len(citations)
    citations.sort()
    for index in range(n):
        h_index = min(citations[index], n-index)
        if h_index > answer:
            answer = h_index    
    
    return answer