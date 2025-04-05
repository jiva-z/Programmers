def solution(k, tangerine):
    tangerineCount = {}
    
    for i in range(len(tangerine)):
        if tangerine[i] in tangerineCount:
            tangerineCount[tangerine[i]] += 1
        else:
            tangerineCount[tangerine[i]] = 1
    
    # 개수가 많은 순서대로 정렬
    sorted_sizes = sorted(tangerineCount.values(), reverse=True)
    
    # 귤을 선택
    total = 0
    kinds = 0
    for count in sorted_sizes:
        if total < k:
            total += count
            kinds += 1
        else:
            break
    
    return kinds