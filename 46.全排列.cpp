/*
 * @lc app=leetcode.cn id=46 lang=cpp
 *
 * [46] 全排列
 */

// @lc code=start
class Solution {
public:
    vector<vector<int>> result;
    vector<bool> used;
    vector<int> tmp;
    int length;

    vector<vector<int>> permute(vector<int>& nums) {
        length = nums.size();
        used.resize(nums.size());
        tmp.resize(length);
        for (int i = 0; i < nums.size(); ++i) {
            used[i] = false;
        }

        process(0, nums);

        return result;
    }

    void process(int idx, vector<int>& nums) {
        if (idx >= length) {
            result.push_back(tmp);
            return;
        }

        for (int i = 0; i < length; ++i) {
            if (!used[i]) {
                used[i] = true;
                tmp[idx] = nums[i];
                process(idx + 1, nums);
                used[i] = false;
            }
        }
    }
};
// @lc code=end

