import java.util.*;

class Solution {
    
    static class Job {
        int id;
        int duration;
        int requestTime;
        
        public Job(int id, int requestTime, int duration){
            this.id = id;
            this.duration = duration;
            this.requestTime = requestTime;
        }
    }
    
    public int solution(int[][] jobs) {
        int answer = 0;
        List<Job> jobList = new ArrayList<>();
        for (int i = 0; i < jobs.length; i++){
            jobList.add(new Job(i, jobs[i][0], jobs[i][1]));
        }
            
        // 1. 작업 리스트 정렬 (요청 시각 기준, 동일할 경우 작업 번호 순)
        Collections.sort(jobList, (a, b) -> {
            if (a.requestTime == b.requestTime){
                return a.id - b.id;
            }
            return (a.requestTime - b.requestTime);
        });
        
        // 2. 우선순위 큐: 소요시간 → 요청시간 → 작업번호 순 정렬
        PriorityQueue<Job> pq = new PriorityQueue<>((a, b) -> {
            if (a.duration != b.duration) return a.duration - b.duration;
            if (a.requestTime != b.requestTime) return a.requestTime - b.requestTime;
            return a.id - b.id;
    });
        
        int currentTime = 0;    // 현재 시간
        int totalResponse = 0;  // 모든 작업의 반환 시간 합계
        int processed = 0;     // 처리 완료된 작업 수
        int index = 0;          // jobList에서 다음으로 처리될 작업의 위치 (대기 큐에 아직 추가되지 않은 작업)
        
        while (processed < jobList.size()) {
            // 현재 시간 이전 요청 작업 큐에 추가
            while (index < jobList.size() &&
                  jobList.get(index).requestTime
                  <= currentTime){
                // 현재 작업 큐에 추가하고 다음 작업을 가리키기 위해 인덱스 증가
                pq.offer(jobList.get(index++));
            }
            
            // 처리 가능한 작업 없는 경우
            if (pq.isEmpty()){
                currentTime = jobList.get(index).requestTime;
            }
            // 작업 처리
            else{
                // 우선순위 큐에서 반환하고 제거
                Job job = pq.poll();
                currentTime += job.duration;
                totalResponse += currentTime - job.requestTime;
                processed++;
            }
        }
        
        // 4. 평균 계산
        answer = totalResponse / jobs.length;
        return answer;
    }
}