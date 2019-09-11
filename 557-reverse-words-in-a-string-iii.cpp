#include <string>

using namespace std;

class Solution {
public:
    string reverseWords(string s) {
        string result = "";
        int curPos = 0;
        while(curPos < s.length()) {
            auto foundPos = s.find_first_of(' ', curPos);
            if (foundPos != string::npos) {
                for (int i = foundPos - 1; i >= curPos; --i) {
                    result.push_back(s[i]);
                }
                result.push_back(' ');
                curPos = foundPos + 1;
            } else {
                for (int i = s.length() - 1; i >= curPos; --i) {
                    result.push_back(s[i]);
                }
                break;
            }
        }
        return result;
    }
};