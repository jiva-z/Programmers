import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        
        // 우선순위 큐
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());

        // 일반 큐
        Queue<Integer> queue = new LinkedList<>();
        
        // 우선순위 큐에 우선순위 값, 일반 큐에 인덱스 넣음
        for (int i = 0; i < priorities.length; i++){
            pq.offer(priorities[i]);
            queue.offer(i);
        }
        
        int order = 0;
        
        while (!queue.isEmpty()){       // 큐가 비어 있지 않으면
            int current = queue.poll(); // 일반 큐의 첫번째 요소 반환하고 제거
            // 현재 프로세스의 우선순위가 가장 높은 경우
            if (priorities[current] == pq.peek()){
                order++;
                pq.poll();  // 우선순위 큐 첫번째 요소 반환하고 제거
                
                if (current == location) {
                   return order; 
                }
            } else {
                // 우선순위가 더 높은 프로세스가 있는 경우 우선순위 큐에 다시 요소 추가
                queue.offer(current);
            }
        }
        return order;
    }
}