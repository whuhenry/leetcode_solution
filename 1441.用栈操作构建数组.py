#
# @lc app=leetcode.cn id=1441 lang=python3
#
# [1441] 用栈操作构建数组
#

from typing import List

# @lc code=start
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        idx_t = 0
        idx_l = 1
        n = len(target)
        result = []
        while idx_t < n:
            result.append('Push')
            if target[idx_t] == idx_l:
                idx_t += 1
            else:
                result.append('Pop')
            idx_l += 1
        return result

# @lc code=end

