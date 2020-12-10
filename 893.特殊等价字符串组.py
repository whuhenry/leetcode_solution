#
# @lc app=leetcode.cn id=893 lang=python3
#
# [893] 特殊等价字符串组
#

from typing import List

# @lc code=start

import collections

class Solution:
    def special_count(self, s):
        return collections.Counter(s[0::2]), collections.Counter(s[1::2])

    def numSpecialEquivGroups(self, A: List[str]) -> int:
        special_A = [self.special_count(a) for a in A]
        result = [0] * len(special_A)
        head = 0
        idx = 0
        while head < len(special_A):
            if result[head] == 0:
                idx += 1
                result[head] = idx
                for i in range(head + 1, len(special_A)):
                    if special_A[i] == special_A[head]:
                        result[i] = idx
            head += 1 

        return len(set(result))
# @lc code=end

s = Solution()
print(s.numSpecialEquivGroups(["abcd","cdab","cbad","xyzz","zzxy","zzyx"]))