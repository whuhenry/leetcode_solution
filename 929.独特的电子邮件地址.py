#
# @lc app=leetcode.cn id=929 lang=python3
#
# [929] 独特的电子邮件地址
#

from typing import List

# @lc code=start
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = set()
        for email in emails:
            name, host = email.split('@')
            plus_loc = name.find('+')
            if plus_loc != -1:
                name = name[0: plus_loc]
            name = name.replace('.', '')
            result.add(name + '@' + host)
        return len(result)
# @lc code=end

s = Solution()
print(s.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))