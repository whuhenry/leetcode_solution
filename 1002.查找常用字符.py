#
# @lc app=leetcode.cn id=1002 lang=python3
#
# [1002] 查找常用字符
#

from typing import List

# @lc code=start
import collections

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        min_count = [1000] * 26
        exist_times = [0] * 26
        for a in A:
            count = collections.Counter(a)
            for k in count:
                idx_k = ord(k) - ord('a')
                min_count[idx_k] = min(min_count[idx_k], count[k])
                exist_times[idx_k] += 1

        result = []
        for i in range(26):
            if exist_times[i] == len(A):
                for j in range(min_count[i]):
                    result.append(chr(i + ord('a')))
        return result

# @lc code=end

s = Solution()
print(s.commonChars(["bella","label","roller"]))