#
# @lc app=leetcode.cn id=997 lang=python3
#
# [997] 找到小镇的法官
#

from typing import List

# @lc code=start
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trust_count = [0] * (N + 1)
        trusted_count = [0] * (N + 1)
        for t in trust:
            trust_count[t[0]] += 1
            trusted_count[t[1]] += 1

        result = -1
        for i in range(1, N + 1):
            if trusted_count[i] == N - 1 and trust_count[i] == 0:
                result = i
        return result
# @lc code=end

