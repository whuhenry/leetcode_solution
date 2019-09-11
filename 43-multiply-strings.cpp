#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string multiply(string num1, string num2) {
        vector<uint32_t> result;
        int l1 = num1.length(), l2 = num2.length();
        result.resize(l1 + l2 - 1);
        for (int i = 0; i < result.size(); ++i) {
            result[i] = 0;
        }
        for (int i = l2 - 1; i >= 0; --i) {
            for (int j = l1 - 1; j >= 0; --j) {
                result[l2 -1 - i + l1 - 1 - j] += (num1[j] - '0') * (num2[i] - '0');
            }
        }
        int curIdx = 0;
        while(curIdx < result.size() - 1 || result[curIdx] >= 10) {
            if (result[curIdx] >= 10) {
                if (curIdx == result.size() - 1) {
                    result.push_back(result[curIdx] / 10);
                    result[curIdx] = result[curIdx] % 10;
                } else {
                    result[curIdx + 1] += result[curIdx] / 10;
                    result[curIdx] = result[curIdx] % 10;
                }
            }
            ++curIdx;
        }
        curIdx = result.size() - 1;
        while(0 == result[curIdx] && curIdx > 0) {
            result.pop_back();
            --curIdx;
        }

        string strResult = "";
        for(int i = result.size() - 1; i >= 0; --i) {
            strResult.push_back(char(result[i] + '0'));
        }
        return strResult;
    }
};