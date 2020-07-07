#include <vector>
using namespace std;
/*
 * @lc app=leetcode.cn id=1295 lang=cpp
 *
 * [1295] 统计位数为偶数的数字
 */

// @lc code=start
class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int count = 0;
        for (int i = 0; i < nums.size(); ++i) {
            int len = (int)log10(nums[i]);
            if (len % 2 == 1) {
                ++count;
            }
        }
        return count;
    }
};
// @lc code=end

