from itertools import permutations

def solution(k, dungeons):
    max_count = 0
    
    # 모든 던전 순서에 대한 순열 생성
    for perm in permutations(dungeons):
        current_fatigue = k
        count = 0
        
        # 현재 순열에 따라 던전을 탐험
        for min_fatigue, consume_fatigue in perm:
            if current_fatigue >= min_fatigue:  # 최소 필요 피로도 충족
                current_fatigue -= consume_fatigue  # 소모 피로도 차감
                count += 1
            else:
                break  # 더 이상 탐험 불가
        
        # 최대 탐험 가능한 던전 수 갱신
        max_count = max(max_count, count)
    
    return max_count
