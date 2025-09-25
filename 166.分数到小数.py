#
# @lc app=leetcode.cn id=166 lang=python3
#
# [166] 分数到小数
#

# @lc code=start
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        flag_minus = ((numerator * denominator) < 0 )
        numerator = abs(numerator)
        denominator = abs(denominator)

        remainders = []
        zhengshu = numerator // denominator
        yushu = numerator % denominator
        xiaoshu  = []
        remainders.append(yushu)
        while yushu != 0:
            xiaoshu.append(str(yushu * 10 // denominator))
            yushu = yushu * 10 % denominator
            if yushu in remainders:
                xiaoshu.append(')')
                xiaoshu.insert(remainders.index(yushu), '(')
                break
            else:
                remainders.append(yushu)

        pre = '-' if flag_minus else ''
        if len(xiaoshu) == 0:
            return pre + str(zhengshu)
        else:
            return f'{pre}{zhengshu}.{"".join(xiaoshu)}'

        
        
        

        
# @lc code=end

s = Solution()
print(s.fractionToDecimal(7, 12))