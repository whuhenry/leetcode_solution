#include <vector>
#include <algorithm>
using namespace std;

/*
 * @lc app=leetcode.cn id=315 lang=cpp
 *
 * [315] 计算右侧小于当前元素的个数
 */

// @lc code=start
class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        int len = nums.size();
        vector<int> result;
        if (0 == len) {
            return result;
        }
        result.resize(len);
        result[len - 1] = 0;
        for (int i = len - 2; i >= 0; --i) {
            // 二分查找
            int begin = i + 1;
            int end = len - 1;
            int target = -1;
            while (begin < end) {
                target = (begin + end) / 2;
                if (nums[target] >= nums[i]) {
                    end = target - 1;
                }
                else {
                    begin = target + 1;
                }
            }
            
            if (begin == end) {
                if (nums[i] > nums[begin]) {
                    target = begin;
                }
                else {
                    target = begin - 1;
                }
            } 
            else {
                if (nums[i] < nums[end]) {
                    target = end - 1;
                }
                else if (nums[i] <= nums[begin]) {
                    target = begin - 1;
                }
                else {
                    target = begin;
                }
            }

            result[i] = target - i;

            int tmp = nums[i];

            for (int j = i; j < target; ++j) {
                nums[j] = nums[j + 1];
            }
            nums[target] = tmp;
        }
        return result;
    }
};
// @lc code=end

