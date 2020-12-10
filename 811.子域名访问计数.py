#
# @lc app=leetcode.cn id=811 lang=python3
#
# [811] 子域名访问计数
#

from typing import List

# @lc code=start

from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_count = defaultdict(int)
        for cpdomain in cpdomains:
            count, domian = cpdomain.split()
            count = int(count)
            domain_parts = domian.split('.')
            domain_count[domain_parts[-1]] += count
            for i in range(len(domain_parts) - 1):
                sub_domain = '.'.join(domain_parts[-(i + 2):len(domain_parts)])
                domain_count[sub_domain] += count
        result = []
        for k in domain_count:
            result.append(str(domain_count[k]) + ' ' + k)
        return result
# @lc code=end

s = Solution()
print(s.subdomainVisits(["9001 discuss.leetcode.com"]))