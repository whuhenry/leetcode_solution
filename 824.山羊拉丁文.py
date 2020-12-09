#
# @lc app=leetcode.cn id=824 lang=python3
#
# [824] 山羊拉丁文
#

# @lc code=start
class Solution:
    def toGoatLatin(self, S: str) -> str:
        s_list = S.split()
        result = []
        vowels = 'aeiouAEIOU'
        for i, word in enumerate(s_list, 1):
            if word[0] in vowels:
                result.append(word + 'ma' + 'a' * i)
            else:
                result.append(word[1:] + word[0] + 'ma' + 'a' * i)
        return ' '.join(result)

        
# @lc code=end

