#
# @lc app=leetcode.cn id=868 lang=python3
#
# [868] 二进制间距
#

# @lc code=start
class Solution:
    def binaryGap(self, n: int) -> int:
        pre = None
        idx = 0
        result = 0
        while n > 0:
            bit = n % 2
            if bit == 1:
                if pre is None:
                    pre = idx
                else:
                    result = max(result, idx - pre)
                    pre = idx

            n = n >> 1
            idx += 1
        return result
# @lc code=end

s = Solution()
print(s.binaryGap(1))