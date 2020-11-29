#
# @lc app=leetcode.cn id=507 lang=python3
#
# [507] 完美数
#

import math

# @lc code=start
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1 or num == 2:
            return False
        sum = 1
        for i in range(2, int(math.sqrt(num)) + 1):
            if i ** 2 == num:
                sum += i
                break
            if num % i == 0:
                sum += i
                sum += num // i
                if sum > num:
                    return False

        if sum == num:
            return True
        return False
        

# @lc code=end

s = Solution()
print(s.checkPerfectNumber(3))
