/*
 * @lc app=leetcode.cn id=1464 lang=cpp
 *
 * [1464] 数组中两元素的最大乘积
 */
#include <vector>
using namespace std;

// @lc code=start
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int len = nums.size();
        int max1 = -1, max2 = -1;
        int idx1 = -1, idx2 = -1;
        for (int i = 0; i < len; ++i) {
            if (nums[i] > max1) {
                max2 = max1;
                idx2 = idx1;
                max1 = nums[i];
                idx1 = i;
                
            } else if (nums[i] > max2) {
                max2 = nums[i];
                idx2 = i;
            }
        }
        return ((nums[idx1] - 1) * (nums[idx2] - 1));
    }
};
// @lc code=end

