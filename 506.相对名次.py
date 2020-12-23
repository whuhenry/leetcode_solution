#
# @lc app=leetcode.cn id=506 lang=python3
#
# [506] 相对名次
#

from typing import List

# @lc code=start
class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        nums_dict = {}
        for i, num in enumerate(nums):
            nums_dict[num] = i
        orders = sorted(nums, reverse=True)
        result = ['' for i in range(len(nums))]
        for i, order in enumerate(orders):
            if i == 0:
                result[nums_dict[order]] = 'Gold Medal'
            elif i == 1:
                result[nums_dict[order]] = 'Silver Medal'
            elif i == 2:
                result[nums_dict[order]] = 'Bronze Medal'
            else:
                result[nums_dict[order]] = str(i + 1)
        return result


# @lc code=end

s = Solution()
s.findRelativeRanks([5, 4, 3, 2, 1])