#
# @lc app=leetcode.cn id=1664 lang=python3
#
# [1664] 生成平衡数组的方案数
#

from typing import List

# @lc code=start
class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        result= 0
        all_sum = sum(nums)
        all_even_sum = 0
        all_odd_sum = 0
        pre_even_sum = []
        pre_odd_sum = []
        for idx, n in enumerate(nums, 0):
            if idx % 2 == 0:
                all_even_sum += n
            else:
                all_odd_sum += n
            pre_even_sum.append(all_even_sum)
            pre_odd_sum.append(all_odd_sum)
            
        for i in range(len(nums)):
            if i % 2 == 0:
                even_sum = pre_even_sum[i] - nums[i] + all_odd_sum - pre_odd_sum[i]
                if even_sum * 2 == all_sum - nums[i]:
                    result += 1
            else:
                odd_sum = pre_odd_sum[i] - nums[i] + all_even_sum - pre_even_sum[i]
                if odd_sum * 2 == all_sum - nums[i]:
                    result += 1
        
        return result



# @lc code=end

