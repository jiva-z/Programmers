public class Solution {
    public int solution(int n) {
        int cnt = 0;
        while(n > 0) {
            if(n % 2 == 1) { // 홀수면 점프 필요
                cnt++;
                n--;
            }
            n /= 2; // 순간이동
        }
        return cnt;
    }
}
