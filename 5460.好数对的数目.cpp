/*
 * @lc app=leetcode.cn id=5460 lang=cpp
 *
 * [5460] 好数对的数目
 */
#include <vector>
using namespace std;

// @lc code=start
class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int len = nums.size();
        int count = 0;
        for (int i = 0; i < len; ++i) {
            for (int j = i + 1; j < len; ++j) {
                if (nums[i] == nums[j]) {
                    ++count;
                }
            }
        }
        return count;
    }
};
// @lc code=end

