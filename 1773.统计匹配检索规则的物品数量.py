#
# @lc app=leetcode.cn id=1773 lang=python3
#
# [1773] 统计匹配检索规则的物品数量
#

from typing import List

# @lc code=start
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == 'type':
            rule = 0
        elif ruleKey == 'color':
            rule = 1
        else:
            rule = 2
        
        result = 0
        for item in items:
            if item[rule] == ruleValue:
                result += 1
        return result

# @lc code=end

