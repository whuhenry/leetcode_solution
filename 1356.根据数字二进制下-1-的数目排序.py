#
# @lc app=leetcode.cn id=1356 lang=python3
#
# [1356] 根据数字二进制下 1 的数目排序
#

from typing import List

# @lc code=start
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def count_bits(n: int):
            result = 0
            while n > 0:
                result += n % 2
                n = n >> 1
            return result
        
        new_arr = [[n, count_bits(n)] for n in arr]
        new_arr.sort(key=lambda x: (x[1], x[0]))
        return [n[0] for n in new_arr]
# @lc code=end

s = Solution()
print(s.sortByBits([0,1,2,3,4,5,6,7,8]))