#
# @lc app=leetcode.cn id=748 lang=python3
#
# [748] 最短补全词
#

from typing import List

# @lc code=start
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        lincese_dict = {}
        for ch in licensePlate:
            if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
                ch = ch.lower()
                if ch in lincese_dict:
                    lincese_dict[ch] += 1
                else:
                    lincese_dict[ch] = 1

        result = None
        
        for word in words:
            word_dict = {}
            flag = True
            for ch in word:
                if 'a' <= ch <= 'z':
                    if ch in word_dict:
                        word_dict[ch] += 1
                    else:
                        word_dict[ch] = 1
            for k in lincese_dict:
                if k not in word_dict or lincese_dict[k] > word_dict[k]:
                    flag = False
                    break
            if flag:
                if result is None:
                    result = word
                else:
                    result = word if len(word) < len(result) else result
        return result

# @lc code=end

s = Solution()
s.shortestCompletingWord("1s3 PSt", ["step","steps","stripe","stepple"])

