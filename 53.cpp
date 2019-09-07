#include<vector>
using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int preMinSum, maxSum, sum;
        int length = nums.size();
        if (0 == length) {
            return 0;
        }
        if (1 == length) {
            return nums[0];
        }
        preMinSum = 0 > nums[0] ? nums[0] : 0;
        maxSum =  nums[0];
        sum =  nums[0];
        for (int i = 1; i < length; ++i) {
            sum += nums[i];
            if (sum - preMinSum > maxSum) {
                maxSum = sum - preMinSum;
            }
            if (sum < preMinSum) {
                preMinSum = sum;
            }
        }

        return maxSum;
    }
};