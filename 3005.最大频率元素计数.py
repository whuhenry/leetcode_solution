#
# @lc app=leetcode.cn id=3005 lang=python3
#
# [3005] 最大频率元素计数
#
from typing import List

# @lc code=start
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        max_freq = max(freq.values())

        re = 0
        for n, freq_n in freq.items():
            if freq_n == max_freq:
                re += freq_n
        return re
        
# @lc code=end
