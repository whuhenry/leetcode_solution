#
# @lc app=leetcode.cn id=2126 lang=python3
#
# [2126] 摧毁小行星
#

from typing import List

# @lc code=start
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for asteroid in asteroids:
            if mass < asteroid:
                return False
            else:
                mass += asteroid
        return True
# @lc code=end

