/*
 * @lc app=leetcode.cn id=264 lang=cpp
 *
 * [264] 丑数 II
 */

// @lc code=start
class Solution {
public:
    int nthUglyNumber(int n) {
        vector<unsigned long> result;
        result.push_back(1);
        int num[3] = {2, 3, 5};
        while(result.size() < n) {
            unsigned long pre = result[result.size() - 1];
            unsigned long minNum = pre * 2;
            for (int i = result.size() - 2; i >= 0; --i ) {
                if (result[i] * 5 < pre) {
                    break;
                }
                for (int j = 0; j < 3; ++j) {
                    unsigned long tmp = result[i] * num[j];
                    if (tmp < minNum && tmp > pre) {
                        minNum = tmp;
                    }
                }
            }
            result.push_back(minNum);
        }

        return result[n - 1];
    }
};
// @lc code=end

