#
# @lc app=leetcode.cn id=874 lang=python3
#
# [874] 模拟行走机器人
#

from typing import List

# @lc code=start
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        ob_set = set(map(tuple, obstacles))
        loc = (0, 0)
        dir = 0   # 0: N, 1: E, 2: S, 3: W
        dir_vec = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        result = 0
        for cmd in commands:
            if cmd == -2:
                dir = (dir - 1 + 4) % 4
            elif cmd == -1:
                dir = (dir + 1) % 4
            else:
                for i in range(cmd):
                    tmp = (loc[0] + dir_vec[dir][0], loc[1] + dir_vec[dir][1])
                    if tmp in ob_set:
                        break
                    else:
                        loc = tmp
                result = max(result, loc[0] ** 2 + loc[1] ** 2)

        return result

# @lc code=end

