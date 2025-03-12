class Solution {
    public String solution(int a, int b) {
        
        // 날짜의 요일을 담은 배열 (2016년 1월 1일은 금요일부터)
        String[] day = {"FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"};
        // 각 월의 일수를 담은 배열
        int[] month = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 30};
        // 총 일 수를 담을 변수
        int answer = 0;
        for (int i = 0; i < a - 1; i++){
            answer += month[i];
        }
        
        // 남은 일수 더하기 (요일 인덱스가 0부터 시작이므로 -1)
        answer += b - 1;
        
        return day[answer % 7];
    }
}