from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        min_pre = 0
        pre_sum = 0
        result = nums[0]
        for num in nums:
            pre_sum += num
            result = max(result, pre_sum - min_pre)
            min_pre = min(pre_sum, min_pre)
        return result