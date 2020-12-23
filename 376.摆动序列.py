#
# @lc app=leetcode.cn id=376 lang=python3
#
# [376] 摆动序列
#

from typing import List

# @lc code=start
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        bigger = [1] * len(nums)
        lowwer = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] > nums[i]:
                    lowwer[i] = max(bigger[j] + 1, lowwer[i])
                elif nums[j] < nums[i]:
                    bigger[i] = max(lowwer[j] + 1, bigger[i])
        return max(max(bigger), max(lowwer))

# @lc code=end

s = Solution()
print(s.wiggleMaxLength([1,7,4,9,2,5]))