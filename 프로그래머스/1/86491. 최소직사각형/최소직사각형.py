def solution(sizes):
    width = []
    height = []
    
    for i in sizes:
        width.append(max(i))    # 가로와 세로 중 긴 길이를 가로 리스트에 저장
        height.append(min(i))   # 가로와 세로 중 짧은 길이를 세로 리스트에 저장
        
    return max(width) * max(height) # 제일 긴 길이 끼리 곱하여 크기 계산