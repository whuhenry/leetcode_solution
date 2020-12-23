#
# @lc app=leetcode.cn id=1399 lang=python3
#
# [1399] 统计最大组的数目
#

# @lc code=start
import collections
class Solution:
    def countLargestGroup(self, n: int) -> int:
        def sum_digits(dig: int):
            result = 0
            while dig > 0:
                result += dig % 10
                dig = dig // 10
            return result

        count_dict = collections.defaultdict(int)
        for i in range(1, n + 1):
            count_dict[sum_digits(i)] += 1
        count_n = collections.Counter(count_dict.values())
        most_common = -1
        result = 0
        for k in count_n:
            if k > most_common:
                most_common = k
                result = count_n[k]
        return result



# @lc code=end

s = Solution()
print(s.countLargestGroup(24))