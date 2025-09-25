#
# @lc app=leetcode.cn id=1805 lang=python3
#
# [1805] 字符串中不同整数的数目
#

# @lc code=start
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        re = set()
        head = 0
        tail = 0
        l = len(word)
        while head < l and tail < l:
            if '0' <= word[tail] <= '9':
                tail += 1
            else:
                if tail > head:
                    re.add(int(word[head:tail]))
                tail += 1
                head = tail
        if tail > head:
            re.add(int(word[head:tail]))
        return len(re)
        
# @lc code=end

