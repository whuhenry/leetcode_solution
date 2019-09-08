#include <vector>

using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        int robbermax, preMax, prepreMax;
        int length = nums.size();
        if (0 == length) {
            return 0;
        }
        if (1 == length) {
            return nums[0];
        }

        preMax = nums[0];
        prepreMax = 0;

        for (int i = 1; i < length; ++i) {
            robbermax = max(nums[i] + prepreMax, preMax);

            prepreMax = preMax;
            preMax = robbermax;
        }

        return robbermax;
    }
};