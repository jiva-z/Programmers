def solution(video_len, pos, op_start, op_end, commands):
    # 초 단위로 변환
    pos_time = int(pos.split(':')[0]) * 60 + int(pos.split(':')[1])
    opStart_time = int(op_start.split(':')[0]) * 60 + int(op_start.split(':')[1])
    opEnd_time = int(op_end.split(':')[0]) * 60 + int(op_end.split(':')[1])
    video_time = int(video_len.split(':')[0]) * 60 + int(video_len.split(':')[1])
    
    # 명령 처리
    for command in commands:
        # 명령 처리 전에 오프닝 구간 확인
        if opStart_time <= pos_time <= opEnd_time:
            pos_time = opEnd_time
        
        # 명령 처리
        if command == 'next':
            pos_time += 10
        elif command == 'prev':
            pos_time -= 10
        
        # 범위 조정
        if pos_time < 0:
            pos_time = 0
        elif pos_time > video_time:
            pos_time = video_time
    
    # 모든 명령 처리 후에도 오프닝 구간 확인
    if opStart_time <= pos_time <= opEnd_time:
        pos_time = opEnd_time
    
    # mm:ss 형식으로 변환
    mm = str(pos_time // 60).zfill(2)  # 두 자리로 만듦
    ss = str(pos_time % 60).zfill(2)  # 두 자리로 만듦
    
    answer = f"{mm}:{ss}"
    
    return answer
