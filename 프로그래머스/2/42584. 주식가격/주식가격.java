import java.util.*;

class Solution {
    public int[] solution(int[] prices) {
        
        int[] answer = new int[prices.length];
        Deque<Integer> stack = new ArrayDeque<>();
        
        // 주식 가격 순회
        for (int i = 0; i < prices.length; i++){
            // 현재 가격이 스택의 최상위 가격보다 낮을 때까지 반복
            
            while (!stack.isEmpty() && prices[i] < prices[stack.peek()]){
                int prevIndex = stack.pop();
                answer [prevIndex] = i - prevIndex; // 시간
            }
            stack.push(i); // 현재 인덱스 스택에 추가
        }
        
        // 스택에 남은 인덱스 처리 (끝까지 가격이 떨어지지 않은 경우)
        while (!stack.isEmpty()){
            int remainIndex = stack.pop();
            answer[remainIndex] = prices.length - 1 - remainIndex;
        }
        
        return answer;
    }
}