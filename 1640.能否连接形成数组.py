#
# @lc app=leetcode.cn id=1640 lang=python3
#
# [1640] 能否连接形成数组
#

from typing import List

# @lc code=start
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        for piece in pieces:
            flag = False
            for i in range(len(arr) - len(piece) + 1):
                if arr[i] == piece[0]:
                    all_eq = True
                    for j in range(1, len(piece)):
                        if arr[i + j] != piece[j]:
                            all_eq = False
                            break
                    flag = all_eq
                    break
            if not flag:
                return False
        return True
                

# @lc code=end

s = Solution()
print(s.canFormArray([37,69,3,74,46], [[37,69,3,74,46]]))