import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        
        // bridge_length 만큼의 크기를 갖는 큐
        Queue <Integer> bridge = new LinkedList<>();
        
        
        // 맨 처음 비어있는 다리 공간 모두를 0으로 초기화
        for (int i = 0; i < bridge_length; i++){
            bridge.offer(0);
        }

        // 다리 길이가 1이거나 트럭의 개수가 1일 경우
        if (bridge_length == 1){
            return truck_weights.length + 1;
        }
        
        if (truck_weights.length == 1){
            return bridge_length + 1;
        }
        
        int idx = 0;
        // 현재 다리에 있는 모든 트럭의 무게
        int totalWeight = 0;
        
        // 트럭의 개수만큼 반복
        while(idx < truck_weights.length){
            // 현재 다리에 존재하는 맨 앞 트럭의 무게 뺌
            totalWeight -= bridge.poll();
            answer++;   // 새로운 트럭 넣음
            
            // 현재 다리에 있는 트럭 무게 + 들어올 트럭 무게 합 과 weight 비교
            if (totalWeight + truck_weights[idx] <= weight){
                bridge.offer(truck_weights[idx]);
                totalWeight += truck_weights[idx++];
            }
            else{
                // 견딜 수 있는 무게보다 커질 경우 0을 넣음
                bridge.offer(0);
            }
        }
        
        // 마지막 트럭까지 다리를 건너는 값 구하기 위해 + bridge_length
        return answer + bridge_length;
    }
} 