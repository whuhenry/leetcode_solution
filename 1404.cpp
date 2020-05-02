class Solution {
public:
    int numSteps(string s) {
        vector<int> nums;
        for (int i = 0; i < s.length(); ++i) {
            nums.push_back(s[i] - '0');
        }
        int result = 0;
        while(nums.size() > 1) {
            if (nums.back() == 1) {
                nums[nums.size() - 1] += 1;
                int ptr = nums.size() - 1;
                while (nums[ptr] > 1 && ptr > 0) {
                    nums[ptr - 1] += 1;
                    nums[ptr] = 0;
                    --ptr;
                }
            } else {
                nums.pop_back();
            }
            ++result;
        }

        if (nums[0] > 1) {
            ++result;
        }

        return result;
    }
};