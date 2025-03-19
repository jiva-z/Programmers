import java.util.*;

class Solution {
    public int solution(int[] people, int limit) {
        Arrays.sort(people);  // 몸무게 오름차순 정렬
        int left = 0, right = people.length - 1;  // 두 포인터
        int answer = 0;
        
        while (left <= right) {
            if (people[left] + people[right] <= limit) {
                left++;  // 가벼운 사람도 태움        
            }
            right--;  // 무거운 사람 태움            
            answer++;  // 보트 하나 추가
        }
        
        return answer;
    }
}
