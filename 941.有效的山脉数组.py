#
# @lc app=leetcode.cn id=941 lang=python3
#
# [941] 有效的山脉数组
#

from typing import List

# @lc code=start
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        top = 0
        
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                return False
            if arr[i] < arr[i - 1]:
                top = i - 1
                break

        if top == 0:
            return False
        for i in range(top + 1, len(arr)):
            if arr[i] >= arr[i - 1]:
                return False
        return True
# @lc code=end

s = Solution()
print(s.validMountainArray([0,3,2,1]))