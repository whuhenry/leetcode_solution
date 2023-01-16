#
# @lc app=leetcode.cn id=2244 lang=python3
#
# [2244] 完成所有任务需要的最少轮数
#

from typing import List

# @lc code=start
from collections import Counter

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        result = 0
        c = Counter(tasks)
        for t in c:
            print(t, c[t])
            result += c[t] // 6 * 2
            count = c[t] % 6
            if count % 2 == 0:
                result += count // 2
            elif count == 1:
                if c[t] < 6:
                    return -1
                else:
                    result += 1
            elif count == 3:
                result += 1
            elif count == 5:
                result += 2
        return result



# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.minimumRounds([66,66,63,61,63,63,64,66,66,65,66,65,61,67,68,66,62,67,61,64,66,60,69,66,65,68,63,60,67,62,68,60,66,64,60,60,60,62,66,64,63,65,60,69,63,68,68,69,68,61]))