class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        int len = nums.size();
        vector<int> sortedNums(nums);
        sort(sortedNums.begin(), sortedNums.end());
        int start = -1, end = len - 1;
        for (int i = 0; i < len; ++i) {
            if (nums[i] != sortedNums[i]) {
                start = i;
                break;
            }
        }
        if (-1 == start) {
            start = len;
        }

        for (int i = len - 1; i >= start; --i) {
            if (nums[i] != sortedNums[i]) {
                end = i;
                break;
            }
        }
        return end - start + 1;
    }
};