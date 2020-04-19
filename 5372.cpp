class Solution {
public:
    int minStartValue(vector<int>& nums) {
        int sum = 0;
        int minSum = nums[0];
        for (int i = 0; i < nums.size(); ++i) {
            sum += nums[i];
            if (sum < minSum) {
                minSum = sum;
            }
        }

        int result = - minSum + 1;
        if (result < 1) {
            result = 1;
        }
        return result;
    }
};