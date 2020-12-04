#
# @lc app=leetcode.cn id=1346 lang=python3
#
# [1346] 检查整数及其两倍数是否存在
#

from typing import List

# @lc code=start
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        Sa = set(arr)
        count_zero = 0
        for num in arr:
            if num != 0 and num * 2 in Sa:
                return True
            elif num == 0:
                count_zero += 1
                if count_zero >= 2:
                    return True
        

        return False
# @lc code=end

