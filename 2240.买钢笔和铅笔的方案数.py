#
# @lc app=leetcode.cn id=2240 lang=python3
#
# [2240] 买钢笔和铅笔的方案数
#

# @lc code=start
class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        result = 0
        min_cost = min(cost1, cost2)
        max_cost = max(cost1, cost2)

        for i in range(total // max_cost + 1):
            left = total - max_cost * i
            result += left // min_cost + 1

        return result
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.waysToBuyPensPencils(5, 10, 10))