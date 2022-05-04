#
# @lc app=leetcode.cn id=1823 lang=python3
#
# [1823] 找出游戏的获胜者
#

# @lc code=start
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        people = list(range(1, n + 1))

        pos = 0
        for i in range(n - 1):
            pos += k - 1
            pos = pos % len(people)
            people.remove(people[pos])
            # print(people)
        return people[0]
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.findTheWinner(500, 200))

