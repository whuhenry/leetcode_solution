#
# @lc app=leetcode.cn id=1496 lang=python3
#
# [1496] 判断路径是否相交
#

# @lc code=start
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        x = 0
        y = 0
        visited.add(20001 * x + y)
        step = {
            'N': [0, 1],
            'S': [0, -1],
            'E': [1, 0],
            'W': [-1, 0]
        }
        for ch in path:
            x += step[ch][0]
            y += step[ch][1]
            loc = 20001 * x + y
            if loc in visited:
                return True
            visited.add(loc)
        return False

# @lc code=end

