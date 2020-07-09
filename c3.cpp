class Solution {
private:
    bool flag[26];
public:
    bool cross(string &a, string &b) {
        for (char cha : a) {
            for (char chb : b) {
                if (cha == chb) {
                    return true;
                }
            }
        }
        return false;
    }

    bool selfCross(string &str) {
        for (int i = 0; i < str.size(); ++i) {
            for (int j = i + 1; j < str.size(); ++j) {
                if (str[i] == str[j]) {
                    return true;
                }
            }
        }
        return false;
    }

    void resetFlag() {
        for (int i = 0; i < 26; ++i) {
            flag[i] = false;
        }
    }

    int maxLen;
    int curLen;
    void search(vector<string> &candidate, int curIdx) {
        if (curIdx >= candidate.size()) {
            if (curLen > maxLen) {
                maxLen = curLen;
            }
            return;
        }
        bool crossed = false;
        for (char ch : candidate[curIdx]) {
            if (flag[ch - 'a']) {
                crossed = true;
            }
        }
        if (crossed) {
            search(candidate, curIdx + 1);
        } else {
            for (char ch : candidate[curIdx]) {
                flag[ch - 'a'] = true;
            }
            curLen += candidate[curIdx].size();
            search(candidate, curIdx + 1);
            curLen -= candidate[curIdx].size();
            for (char ch : candidate[curIdx]) {
                flag[ch - 'a'] = false;
            }
            search(candidate, curIdx + 1);
        }
    }

    int maxLength(vector<string>& arr) {
        int len = arr.size();
        int baseAns = 0;
        vector<string> candidate;
        maxLen = 0;
        curLen = 0;
        for (int i = 0; i < len; ++i) {
            if (selfCross(arr[i])) {
                continue;
            }
            bool unique = true;
            for (int j = 0; j < len; ++j) {
                if (i != j) {
                    if (cross(arr[i], arr[j])) {
                        unique = false;
                        break;
                    }
                }
            }
            if (unique) {
                baseAns += arr[i].size();
            } else {
                candidate.push_back(arr[i]);
            }
        }

        resetFlag();
        search(candidate, 0);
        return maxLen + baseAns;

    }
};