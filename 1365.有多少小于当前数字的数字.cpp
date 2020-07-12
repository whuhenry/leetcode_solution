#include<vector>
using namespace std;
/*
 * @lc app=leetcode.cn id=1365 lang=cpp
 *
 * [1365] 有多少小于当前数字的数字
 */

// @lc code=start
class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        vector<int> result;
        for (int i = 0; i < nums.size(); ++i) {
            int count = 0;
            for (int j = 0; j < nums.size(); ++j) {
                if (j != i && nums[j] < nums[i]) {
                    ++count;
                }
            }
            result.push_back(count);
        }
        return result;
    }
};
// @lc code=end

