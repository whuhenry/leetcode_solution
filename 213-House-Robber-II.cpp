#include <vector>

using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        int preMax, prepreMax;
        int length = nums.size();
        if (0 == length) {
            return 0;
        }
        if (1 == length) {
            return nums[0];
        }
        if (2 == length) {
            return max(nums[0], nums[1]);
        }


        // rob 0 ~ length - 1
        preMax = nums[0];
        prepreMax = 0;
        int robbermax1 = 0;
        for (int i = 1; i < length - 1; ++i) {
            robbermax1 = max(nums[i] + prepreMax, preMax);

            prepreMax = preMax;
            preMax = robbermax1;
        }

        // rob 1 ~ length
        preMax = nums[1];
        prepreMax = 0;
        int robbermax2 = 0;
        for (int i = 2; i < length; ++i) {
            robbermax2 = max(nums[i] + prepreMax, preMax);

            prepreMax = preMax;
            preMax = robbermax2;
        }

        return max(robbermax1, robbermax2);
    }
};