#
# @lc app=leetcode.cn id=984 lang=python3
#
# [984] 不含 AAA 或 BBB 的字符串
#

# @lc code=start
class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        a1 = a
        a2 = 0
        b1 = b
        b2 = 0
        if a < b:
            b2 = b - a
        else:
            a2 = a - b
        
        ca = 0
        cb = 0
        s = ''

        for i in range(min(a, b)):
            if a > b:
                if a2 > 0:
                    s += 'aa'
                    a2 -= 1
                    ca += 2
                else:
                    s += 'a'
                    a1 -= 1
                    ca += 1
                
                if b2 > 0:
                    s += 'bb'
                    b2 -= 1
                    cb += 2
                else:
                    s += 'b'
                    b1 -= 1
                    cb += 1
            else:
                if b2 > 0:
                    s += 'bb'
                    b2 -= 1
                    cb += 2
                else:
                    s += 'b'
                    b1 -= 1
                    cb += 1
                if a2 > 0:
                    s += 'aa'
                    a2 -= 1
                    ca += 2
                else:
                    s += 'a'
                    a1 -= 1
                    ca += 1
                
                

        s += 'a' * (a - ca) + 'b' * (b - cb)

        

        return s

# @lc code=end

