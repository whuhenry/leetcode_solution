#
# @lc app=leetcode.cn id=2243 lang=python3
#
# [2243] 计算字符串的数字和
#

# @lc code=start

class Solution:
    def digitSum(self, s: str, k: int) -> str:

        while len(s) > k:
            t = []
            iter_count = len(s) // k
            if 0 != len(s) % k:
                iter_count += 1


            for i in range(iter_count):
                sub_s = s[i * k : min((i + 1) * k, len(s))]
                t.append(str(sum(list(map(int, sub_s)))))
            s = ''.join(t)
        return s
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.digitSum("1234", 2))