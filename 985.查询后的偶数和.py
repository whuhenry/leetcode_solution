#
# @lc app=leetcode.cn id=985 lang=python3
#
# [985] 查询后的偶数和
#

from typing import List

# @lc code=start
class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = 0
        for a in A:
            if a % 2 == 0:
                even_sum += a

        result = []
        for query in queries:
            val = query[0]
            idx = query[1]
            if A[idx] % 2 == 0:
                even_sum -= A[idx]
            A[idx] += val
            if A[idx] % 2 == 0:
                even_sum += A[idx]
            result.append(even_sum)
        return result
# @lc code=end

