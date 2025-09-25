#
# @lc app=leetcode.cn id=398 lang=python3
#
# [398] 随机数索引
#

from typing import List

# @lc code=start
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.map = {}
        for idx, n in enumerate(nums):
            if n in self.map:
                self.map[n].append(idx)
            else:
                self.map[n] = [idx]

    def pick(self, target: int) -> int:
        return random.choice(self.map[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
# @lc code=end

