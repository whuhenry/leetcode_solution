#
# @lc app=leetcode.cn id=1287 lang=python3
#
# [1287] 有序数组中出现次数超过25%的元素
#

from typing import List

# @lc code=start
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        candidates = [n // 4, n // 2, int(n * 0.75)]
        for candidate in candidates:
            num = arr[candidate]
            count = 0
            cur = candidate
            while cur < n and arr[cur] == num:
                cur += 1
                count += 1
            cur = candidate - 1
            while cur >= 0 and arr[cur] == num:
                cur -= 1
                count += 1
            if count > n * 0.25:
                return num
        return 0
# @lc code=end

