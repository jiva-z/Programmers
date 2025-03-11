class Solution {
public int solution(int[] schedules, int[][] timelogs, int startday) {
int answer = schedules.length; // 모든 직원이 상품 받을 자격 있다고 가정
    for (int i = 0; i < schedules.length; i++) {
        boolean eligible = true; // 해당 직원의 상품 자격 여부
        int scheduleTime = schedules[i]; // 출근 희망 시각
        int scheduleH = scheduleTime / 100; // 시간(HH)
        int scheduleM = scheduleTime % 100; // 분(MM)
        int scheduleTotal = scheduleH * 60 + scheduleM; // 총 분으로 변환
        int allowedTotal = scheduleTotal + 10; // 허용 범위: 출근 희망 시각 + 10분

        for (int j = 0; j < 7; j++) { // 이벤트 기간 동안 모든 날짜 확인
            int currentDay = (startday - 1 + j) % 7 + 1; // 현재 요일 계산
            if (currentDay > 5) { // 주말(토요일, 일요일)이면 검사 건너뜀
                continue;
            }

            int logTime = timelogs[i][j]; // 실제 출근 기록
            int logH = logTime / 100; // 시간(HH)
            int logM = logTime % 100; // 분(MM)
            int logTotal = logH * 60 + logM; // 총 분으로 변환

            if (logTotal > allowedTotal) { // 허용 범위를 초과하면 자격 박탈
                eligible = false;
                break; // 더 이상 검사할 필요 없음
            }
        }

        if (!eligible) { // 자격 박탈된 경우 정답 감소
            answer--;
        }
    }

    return answer; // 남아 있는 자격 있는 직원 수 반환
}
}