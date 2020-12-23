#
# @lc app=leetcode.cn id=1394 lang=python3
#
# [1394] 找出数组中的幸运数
#

from typing import List

# @lc code=start

import collections
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr_count = collections.Counter(arr)
        result = -1
        for k in arr_count:
            if k == arr_count[k] and k > result:
                result = k
        return result
# @lc code=end

