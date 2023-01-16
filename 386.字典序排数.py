#
# @lc app=leetcode.cn id=386 lang=python3
#
# [386] 字典序排数
#

from typing import List

# @lc code=start

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        self.cur_num = 0

        def checkadd(a):
            self.cur_num = self.cur_num * 10 + a
            if self.cur_num > n:
                self.cur_num = (self.cur_num - a) // 10
                return False
            result.append(self.cur_num)
            return True


        for i1 in range(1, 10):
            if not checkadd(i1):
                break
            for i2 in range(10):
                if not checkadd(i2):
                    break
                for i3 in range(10):
                    if not checkadd(i3):
                        break
                    for i4 in range(10):
                        if not checkadd(i4):
                            break
                        for i5 in range(10):
                            if not checkadd(i5):
                                break
                            self.cur_num = (self.cur_num - i5) // 10
                        self.cur_num = (self.cur_num - i4) // 10
                    self.cur_num = (self.cur_num - i3) // 10
                self.cur_num = (self.cur_num - i2) // 10
            self.cur_num = (self.cur_num - i1) // 10
        return result

# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.lexicalOrder(110))