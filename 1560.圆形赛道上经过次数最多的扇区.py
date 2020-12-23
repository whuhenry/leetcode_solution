#
# @lc app=leetcode.cn id=1560 lang=python3
#
# [1560] 圆形赛道上经过次数最多的扇区
#

from typing import List

# @lc code=start
class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        sector = [0 for i in range(n)]
        pre = None
        sector[rounds[0] - 1] = 1
        for round in rounds:
            if pre is not None:
                cur = pre + 1
                if cur > n:
                    cur = 1
                while cur != round:
                    sector[cur - 1] += 1
                    cur += 1
                    if cur > n:
                        cur = 1
                sector[round - 1] += 1
            pre = round
        max_visist = max(sector)
        result = []
        for i, visit_count in enumerate(sector):
            if visit_count == max_visist:
                result.append(i + 1)
        return result
# @lc code=end

s = Solution()
print(s.mostVisited(2, [2,1,2,1,2,1,2,1,2]))