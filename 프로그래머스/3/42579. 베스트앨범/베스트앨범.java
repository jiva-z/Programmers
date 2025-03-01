import java.util.*;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        // 베스트 앨범에 들어갈 노래의 고유 번호를 저장할 리스트
        ArrayList<Integer> answer = new ArrayList<>();
        
        // 노래 고유번호 , 재생 횟수
        HashMap<String, HashMap<Integer,Integer>> music = new HashMap<>();
        
        // 장르의 총 재생 횟수
        HashMap<String,Integer> num = new HashMap<>();      
        
        
        for (int i = 0; i < plays.length; i++){
            
            if (!num.containsKey(genres[i])) {                // num Map에 없는 장르인 경우
                HashMap<Integer,Integer> map = new HashMap<>();
                
                map.put(i , plays[i]);
                music.put(genres[i] , map);
                num.put(genres[i] , plays[i]);
            }
            else {
                music.get(genres[i]).put(i , plays[i]);
                num.put(genres[i], num.get(genres[i]) + plays[i]);                
            }
        }
        
            // 장르의 총 재생 횟수를 내림차순으로 정렬
            List<String> keySet = new ArrayList(num.keySet());
            Collections.sort(keySet, (s1,s2) -> num.get(s2) - (num.get(s1)));

            // 노래의 총 재생 횟수를 내림차순으로 정렬
            for (String key : keySet){
                HashMap<Integer,Integer> map = music.get(key);
                List<Integer> music_key = new ArrayList(map.keySet());
                Collections.sort(music_key, (s1, s2) -> map.get(s2) - (map.get(s1)));

                answer.add(music_key.get(0));

                if (music_key.size() > 1){  // 노래가 두 곡 이상인 경우
                    answer.add(music_key.get(1));
                }
            }

            return answer.stream().mapToInt(i -> i).toArray();
        
    }
}