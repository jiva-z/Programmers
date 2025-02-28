import java.util.Map;
import java.util.HashMap;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;     // 조합 곱해야되니까
        
        Map<String, Integer> map = new HashMap<>();
        
        for(String[] cloth : clothes){
            map.put(cloth[1], map.getOrDefault(cloth[1],0) + 1);
        }
        
        for(String key : map.keySet()) {    // 모든 조합 계산
            answer *= (map.get(key) + 1);   
        }
        
        answer -= 1;
        
        return answer;
    }
}