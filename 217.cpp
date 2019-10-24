class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        int count = nums.size();
        if (count < 2) {
            return false;
        }
        sort(nums.begin(), nums.end());
        for (int i = 1; i < count; ++i) {
            if (nums[i] == nums[i - 1]) {
                return true;
            }
        }

        return false;
    }
};