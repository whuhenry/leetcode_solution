//需要注意很多细节，比如空字符串，以及最后一个子字符串

class Solution {
public:
    void resetOccur(bool *charOccur) {
        for (int i = 0; i < 256; ++i) {
            charOccur[i] = false;
        }
    }
    
    int lengthOfLongestSubstring(string s) {
        bool charOccur[256];
        resetOccur(charOccur);
        
        int length = s.length();
        int maxLength = -1;
        int curStart = 0;
        for (int i = 0; i < length; ++i) {
            if (charOccur[s[i]]) {
                if (i - curStart > maxLength) {
                    maxLength = i - curStart;
                }
                for (int j = curStart; j < i; ++j) {
                    if (s[j] == s[i]) {
                        curStart = j + 1;
                        break;
                    } else {
                        charOccur[s[j]] = false;
                    }
                }
            } else {
                charOccur[s[i]] = true;
            }
        }
        if (length - curStart > maxLength) {
            maxLength = length - curStart;
        }

        return maxLength;
    }
};