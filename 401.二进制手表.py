#
# @lc app=leetcode.cn id=401 lang=python3
#
# [401] 二进制手表
#

from typing import List

# @lc code=start
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        def gettime():
            hour = sum(self.hour[i] * self.led[i] for i in range(4))
            minite = sum(self.minite[i] * self.led[i + 4] for i in range(6))
            if hour > 11 or minite > 59:
                return None
            return f"{hour}:{minite:02d}"

        def dfs(n: int, pos: int):
            if n == num:
                time = gettime()
                if time is not None:
                    self.result.append(time)
                return
            else:
                for i in range(pos, 10):
                    self.led[i] = 1
                    dfs(n + 1, i + 1)
                    self.led[i] = 0
                


        self.hour = [8, 4, 2, 1]
        self.minite = [32, 16, 8, 4, 2, 1]
        self.led = [0] * 10
        self.result = []
        dfs(0, 0)
        return self.result

# @lc code=end

