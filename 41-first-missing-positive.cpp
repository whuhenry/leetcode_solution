#include <vector>
using namespace std;

class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int count = nums.size();
        if (0 == count) {
            return 1;
        }

        int preMin = (nums[0] == 1 ? 2 : 1)
        for (int i = 1; i < count; ++i) {
            preMin = 
        }
    }
};