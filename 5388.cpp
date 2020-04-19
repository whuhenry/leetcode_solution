class Solution {
public:
    string reformat(string s) {
        int numChar = 0, numNum = 0;
        for (int i = 0; i < s.length(); ++i) {
            if (s[i] >= '0' && s[i] <= '9') {
                ++numNum;
            }
            else if (s[i] >= 'a' && s[i] <= 'z') {
                ++numChar;
            }
        }
        if (abs(numChar - numNum) > 1) {
            return "";
        }
        bool chStart = true;
        if (numNum > numChar) {
            chStart = false;
        }
        int ptrChar = 0, ptrNum = 0;
        string result = "";
        while (ptrChar < s.length() || ptrNum < s.length()) {
            while (ptrChar < s.length() && (s[ptrChar] >= '0' && s[ptrChar] <= '9')) {
                ++ptrChar;
            }
            while (ptrNum < s.length() && (s[ptrNum] >= 'a' && s[ptrNum] <= 'z')) {
                ++ptrNum;
            }
            if (chStart) {
                if (ptrChar < s.length()) {
                    result += s[ptrChar];
                    ++ptrChar;
                }
                if (ptrNum < s.length()) {
                    result += s[ptrNum];
                    ++ptrNum;
                }
            }
            else {
                if (ptrNum < s.length()) {
                    result += s[ptrNum];
                    ++ptrNum;
                }
                if (ptrChar < s.length()) {
                    result += s[ptrChar];
                    ++ptrChar;
                }
            }
        }
        return result;
    }
};