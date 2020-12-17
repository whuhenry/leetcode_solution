#
# @lc app=leetcode.cn id=659 lang=python3
#
# [659] 分割数组为连续子序列
#

from typing import List

# @lc code=start
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        sub_arrs = []
        for num in nums:
            flag = False
            for i in range(len(sub_arrs) - 1, -1, -1):
                if sub_arrs[i][-1] + 1 == num:
                    sub_arrs[i].append(num)
                    flag = True
                    break
                elif sub_arrs[i][-1] + 1 < num:
                    break
            if not flag:
                sub_arrs.append([num])
        for arr in sub_arrs:
            if len(arr) < 3:
                return False
        return True

# @lc code=end

