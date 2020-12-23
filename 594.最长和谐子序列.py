#
# @lc app=leetcode.cn id=594 lang=python3
#
# [594] 最长和谐子序列
#

from typing import List

# @lc code=start
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        num_count = {}
        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1
        result = 0

        keys = list(num_count.keys())
        keys.sort()
        for i in range(1, len(keys)):
            if keys[i] - keys[i - 1] == 1:
                result = max(result, num_count[keys[i]] + num_count[keys[i - 1]])
        return result
# @lc code=end

