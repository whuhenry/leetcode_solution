#
# @lc app=leetcode.cn id=1566 lang=python3
#
# [1566] 重复至少 K 次且长度为 M 的模式
#

from typing import List

# @lc code=start
class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)
        for i in range(n - m * k + 1):
            flag = True
            for j in range(1, k):
                if arr[i: i + m] != arr[i + m * j: i + m * (j + 1)]:
                    flag = False
                    break
            if flag:
                return True
        return False


# @lc code=end

