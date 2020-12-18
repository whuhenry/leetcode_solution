#
# @lc app=leetcode.cn id=1652 lang=python3
#
# [1652] 拆炸弹
#

from typing import List

# @lc code=start
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n        
        new_sum = 0
        step = k // abs(k)
        idx = 0
        for i in range(abs(k)):
            idx = (idx + step + n) % n
            new_sum += code[idx]
        result = [new_sum]
        for i in range(1, n):
            if k > 0:
                new_sum -= code[i]
                idx = (idx + step + n) % n
                new_sum += code[idx]
            else:
                new_sum += code[i - 1]
                new_sum -= code[idx]
                idx = (idx - step + n) % n
            result.append(new_sum)
        return result


# @lc code=end

s = Solution()
print(s.decrypt([2,4,9,3], -2))