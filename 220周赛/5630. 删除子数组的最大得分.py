from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        pre_num_loc = [-1] * 10001
        pre_num_loc[nums[0]] = 0
        pre_sum = [0] * len(nums)
        pre_sum[0] = nums[0]
        pre_most = 0
        pre_most_loc = -1
        result = nums[0]
        for i in range(1, n):
            pre_sum[i] = pre_sum[i - 1] + nums[i]
            if pre_num_loc[nums[i]] > pre_most_loc:
                pre_most = pre_sum[pre_num_loc[nums[i]]]
                pre_most_loc = pre_num_loc[nums[i]]

            pre_num_loc[nums[i]] = i
            result = max(result, pre_sum[i] - pre_most)
        return result

s = Solution()
print(s.maximumUniqueSubarray([5]))
