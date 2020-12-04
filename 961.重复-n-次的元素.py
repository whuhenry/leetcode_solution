#
# @lc app=leetcode.cn id=961 lang=python3
#
# [961] 重复 N 次的元素
#

from  typing import List

# @lc code=start
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        Sa = set()
        for a in A:
            if a in Sa:
                return a
            else:
                Sa.add(a)
        return 0
# @lc code=end

