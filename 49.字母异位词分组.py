#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

from typing import List

# @lc code=start

import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        result_dict = {}
        max_idx = 0
        for word in strs:
            word_count = sorted(list(collections.Counter(word).items()))
            word_hash = ''.join([ch[0] + str(ch[1]) for ch in word_count])
            if word_hash in result_dict:
                result[result_dict[word_hash]].append(word)
            else:
                result_dict[word_hash] = max_idx
                max_idx += 1
                result.append([word])

        return result

# @lc code=end

s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))