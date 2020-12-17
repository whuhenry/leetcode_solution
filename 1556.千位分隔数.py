#
# @lc app=leetcode.cn id=1556 lang=python3
#
# [1556] 千位分隔数
#

# @lc code=start
class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n == 0:
            return '0'
        result = []
        count = 0
        while n > 0:
            result.append(str(n % 10))
            n //= 10
            count += 1
            if count == 3:
                result.append('.')
                count = 0
        if result[-1] == '.':
            result.pop()
        return ''.join(result[::-1])
# @lc code=end

