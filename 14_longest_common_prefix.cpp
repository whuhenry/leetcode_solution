class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (0 == strs.size()) return "";
        
        int shortestLength = strs[0].length();
        for (int i = 1; i < strs.size(); ++i) {
            if (strs[i].length() < shortestLength) {
                shortestLength = strs[i].length();
            }
        }
        
        stringstream ss;
        for (int i = 0; i < shortestLength; ++i) {
            char tmp = strs[0][i];
            bool same = true;
            for (int j = 1; j < strs.size(); ++j) {
                if (tmp != strs[j][i]) {
                    same = false;
                    break;
                }
            }
            if (same) {
                ss << tmp;
            } else {
                break;
            }
        }
        
        return ss.str();
    }
};