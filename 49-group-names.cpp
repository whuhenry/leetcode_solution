#include <vector>
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<string> uniqueStr;
        vector<vector<string>> result;
        for (int i = 0; i < strs.size(); ++i) {
            string str = strs[i];
            sort(str.begin(), str.end());
            bool isNew = true;
            for (int j = 0; j < uniqueStr.size(); ++j) {
                if (uniqueStr[j] == str) {
                    isNew = false;
                    result[j].push_back(strs[i]);
                    break;
                }
            }
            if (isNew) {
                uniqueStr.push_back(str);
                result.push_back({strs[i]});
            }
        }
        return result;
    }
};