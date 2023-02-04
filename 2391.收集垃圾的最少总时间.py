#
# @lc app=leetcode.cn id=2391 lang=python3
#
# [2391] 收集垃圾的最少总时间
#
from typing import List
from collections import Counter

# @lc code=start
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        p, g, m, pe, ge, me = 0, 0, 0, 0, 0, 0
        pgap, ggap, mgap = 0, 0, 0
        travel.append(0)
        for idx, gar in enumerate(garbage):
            c = Counter(gar)
            p += c['P']
            g += c['G']
            m += c['M']
            if c['P'] > 0:
                pe += pgap
                pgap = travel[idx]
            else:
                pgap += travel[idx]
            if c['G'] > 0:
                ge += ggap
                ggap = travel[idx]
            else:
                ggap += travel[idx]
            if c['M'] > 0:
                me += mgap
                mgap = travel[idx]
            else:
                mgap += travel[idx]

        return p + g + m + pe + ge + me

        
        
# @lc code=end

