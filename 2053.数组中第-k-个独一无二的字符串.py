#
# @lc app=leetcode.cn id=2053 lang=python3
#
# [2053] 数组中第 K 个独一无二的字符串
#

from typing import List

# @lc code=start
from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distinct_str = Counter(arr)
        for s in arr:
            if distinct_str[s] == 1:
                k -= 1
                if k == 0:
                    return s
        
        return ""

# @lc code=end