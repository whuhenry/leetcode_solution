class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;
        int result = -1;
        while (left < right) {
            int center = (left + right) / 2;
            if (nums[center] == target) {
                return center;
            }
            if (nums[left] < nums[right]) {
                if (nums[center] < target) {
                    left = center + 1;
                } else {
                    right = center - 1;
                }
            } else {
                if (nums[left] <= nums[center]){
                    if (nums[left] <= target && target <= nums[center]) {
                        right = center - 1;
                    } else {
                        left = center + 1;
                    }                    
                } else {
                    if (nums[center] <= target && target <= nums[right]) {
                        left = center + 1;
                    } else {
                        right = center - 1;
                    }
                }
            }
        }

        if (left >= 0 && left < nums.size() && target == nums[left]) {
            return left;
        }
        if (right >= 0 && right < nums.size() && target == nums[right]) {
            return right;
        }

        return -1;
    }
};