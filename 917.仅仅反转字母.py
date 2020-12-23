#
# @lc app=leetcode.cn id=917 lang=python3
#
# [917] 仅仅反转字母
#

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        result = list(S)
        head = 0
        tail = len(S) - 1
        while head < tail:
            while head < len(S) and not ('a' <= result[head] <= 'z' or 'A' <= result[head] <= 'Z'):
                head += 1
            while tail >= 0 and not ('a' <= result[tail] <= 'z' or 'A' <= result[tail] <= 'Z'):
                tail -= 1
            if head >= tail:
                break
            result[head], result[tail] = result[tail], result[head]
            head += 1
            tail -= 1
        return ''.join(result)
# @lc code=end

s = Solution()
print(s.reverseOnlyLetters("Test1ng-Leet=code-Q!"))