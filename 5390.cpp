#include <string>
#include <map>
#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int minNumberOfFrogs(string croakOfFrogs) {
        vector<int> croakCount(5, 0);
        map<char, int> chIdx;
        chIdx['c'] = 0;
        chIdx['r'] = 1;
        chIdx['o'] = 2;
        chIdx['a'] = 3;
        chIdx['k'] = 4;
        int maxCount = 0;
        for (int i = 0; i < croakOfFrogs.length(); ++i) {
            ++croakCount[chIdx[croakOfFrogs[i]]];
            if ('c' == croakOfFrogs[i]) {
                if (croakCount[0] > maxCount) {
                    maxCount = croakCount[0];
                }
            }
            if ('k' == croakOfFrogs[i]) {
                for (int j = 0; j < 5; ++j) {
                    --croakCount[j];
                }
            }

            // check valid
            for (int j = 0; j < 4; ++j) {
                if (croakCount[j] < croakCount[j + 1]) {
                    return -1;
                }
            }
        }

        for (int j = 0; j < 5 ; ++j) {
            if (croakCount[j] != 0) {
                return -1;
            }
        }

        return maxCount;
    }
};

int main() {
    Solution s;
    cout << s.minNumberOfFrogs("croakcroa") << endl;
}