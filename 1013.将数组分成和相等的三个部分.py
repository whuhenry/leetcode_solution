#
# @lc app=leetcode.cn id=1013 lang=python3
#
# [1013] 将数组分成和相等的三个部分
#

from typing import List

# @lc code=start
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        sum_pre = 0
        sumA = []
        for a in A:
            sum_pre += a
            sumA.append(sum_pre)
        if sum_pre % 3 != 0:
            return False
        flag1, flag2 = False, False
        target1 = sum_pre // 3
        target2 = target1 * 2
        for i in range(0, len(sumA) - 1):
            if (not flag1) and sumA[i] ==  target1:
                flag1 = True
                continue
            if flag1 and sumA[i] == target2:
                flag2 = True
                break
        return flag1 and flag2

# @lc code=end

s = Solution()
print(s.canThreePartsEqualSum([10,-10,10,-10,10,-10,10,-10]))