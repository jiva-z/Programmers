import java.util.PriorityQueue;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        
        // 모든 요소를 큐에 추가 (자동 오름차순 정렬)
        for (int s : scoville) {
            pq.offer(s);
        }

        while (pq.peek() < K) {  // 제일 위에 있는 요소가 K 보다 작으면
            if (pq.size() < 2) { // 요소가 1개 이하면 불가능
                return -1;
            }
            
            int first = pq.poll();  // 가장 작은 값
            int second = pq.poll(); // 두 번째 작은 값
            pq.offer(first + (second * 2)); // 새 스코빌 계산
            answer++;
        }
        
        return answer;
    }
}