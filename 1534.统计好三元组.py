#
# @lc app=leetcode.cn id=1534 lang=python3
#
# [1534] 统计好三元组
#

from typing import List

# @lc code=start
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        arr_len = len(arr)
        result = 0
        for i in range(arr_len):
            for j in range(i + 1, arr_len):
                for k in range(j + 1, arr_len):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        result += 1
        return result
# @lc code=end

