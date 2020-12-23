#
# @lc app=leetcode.cn id=1331 lang=python3
#
# [1331] 数组序号转换
#

from typing import List

# @lc code=start
import collections
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr_count = collections.Counter(arr)
        arr_count_list = list(arr_count.items())
        arr_count_list.sort()

        sum_count = 1
        arr_count = {}
        for n in arr_count_list:
            arr_count[n[0]] = sum_count
            sum_count += 1
        return [arr_count[n] for n in arr]
        
        
# @lc code=end

