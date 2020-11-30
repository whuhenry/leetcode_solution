#
# @lc app=leetcode.cn id=605 lang=python3
#
# [605] 种花问题
#

from typing import List
import math

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        non_flower_count = 0
        max_new_flower = 0
        left_none = True

        for flower in flowerbed:
            if flower == 0:
                non_flower_count += 1
            else:
                if left_none:
                    max_new_flower += math.ceil(max(0, (non_flower_count - 1)) / 2)
                else:
                    max_new_flower += math.ceil(max(0, (non_flower_count - 2)) / 2)
                non_flower_count = 0
                left_none = False
        
        if left_none:
            max_new_flower += math.ceil(max(0, non_flower_count) / 2)
        else:
            max_new_flower += math.ceil(max(0, (non_flower_count - 1)) / 2)
        
        return n <= max_new_flower



# @lc code=end

