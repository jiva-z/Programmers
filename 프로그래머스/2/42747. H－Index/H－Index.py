def solution(citations):
    answer = 0
    
    n = len(citations)
    citations.sort()
    answer = citations[int(len(citations)/2)]
    
    return answer