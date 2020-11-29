#
# @lc app=leetcode.cn id=414 lang=python3
#
# [414] 第三大的数
#

from typing import List

# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        result = [float('-inf'), float('-inf'), float('-inf')]
        for num in nums:
            if num > result[2] and num not in result:
                result[2] = num
                if result[2] > result[1]:
                    result[1], result[2] = result[2], result[1]
                    if result[1] > result[0]:
                        result[0], result[1] = result[1], result[0]
        if result[2] == float('-inf'):
            return result[0]
        else:
            return result[2]
                
# @lc code=end

s = Solution()
s.thirdMax([3, 2, 1])