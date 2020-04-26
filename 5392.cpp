class Solution {
public:
    int maxScore(string s) {
        int count0 = 0, count1 = 0;
        for (int i = 0; i < s.length(); ++i) {
            if ('0' == s[i]) {
                ++count0;
            }else{
                ++count1;
            }
        }
        
        int curCount0 = 0, curCount1 = 0;
        int maxScore = -1;
        for (int i = 0; i < s.length() - 1; ++i) {
            if ('0' == s[i]) {
                ++curCount0;
            }else{
                ++curCount1;
            }
            int score = curCount0 + count1 - curCount1;
            if (score > maxScore) {
                maxScore = score;
            }
        }
        
        return maxScore;
    }
};