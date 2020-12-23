#
# @lc app=leetcode.cn id=717 lang=python3
#
# [717] 1比特与2比特字符
#

from typing import List

# @lc code=start
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits) >= 2:
            if bits[-1] == 0 and bits[-2] == 0:
                return True
            if bits[-1] == 0 and bits[-2] == 1:
                count = 0
                idx = -2
                while idx >= -len(bits):
                    if bits[idx] == 1:
                        count += 1
                    else:
                        break
                    idx -= 1
                if count % 2 == 0:
                    return True
        if len(bits) == 1 and bits[-1] == 0:
            return True
        return False
# @lc code=end

