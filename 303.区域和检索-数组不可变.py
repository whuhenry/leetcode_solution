#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#

from typing import List

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums_sum = [0] * len(nums)
        for i, num in enumerate(nums):
            if i == 0:
                self.nums_sum[i] = num
            else:
                self.nums_sum[i] = num + self.nums_sum[i - 1]

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.nums_sum[j]
        else:
            return self.nums_sum[j] - self.nums_sum[i - 1]




# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
# @lc code=end

