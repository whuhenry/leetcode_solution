#
# @lc app=leetcode.cn id=1360 lang=python3
#
# [1360] 日期之间隔几天
#

# @lc code=start
class Solution:
    def isLeapYear(self, year):
        if year % 4 == 0 and year % 100 != 0:
            return True
        if year % 400 == 0:
            return True
        return False

    def daysBetweenDates(self, date1: str, date2: str) -> int:
        if date1 > date2:
            date1, date2 = date2, date1
        date1 = list(map(int, date1.split('-')))
        date2 = list(map(int, date2.split('-')))
        month = [30] * 12
        for i in [1, 3, 5, 7, 8, 10, 12]:
            month[i - 1] = 31
        month[1] = 28

        result = 0
        for year in range(date1[0] + 1, date2[0]):
            if self.isLeapYear(year):
                result += 366
            else:
                result += 365

        if date1[0] == date2[0]:
            date1, date2 = date2, date1
        
        date_to_end = 0
        for i in range(date1[1], 12):
            if i == 1 and self.isLeapYear(date1[0]):
                date_to_end += 29
            else:
                date_to_end += month[i]
        if date1[1] == 2 and self.isLeapYear(date1[0]):
            date_to_end += 29 - date1[2]
        else:
            date_to_end += month[date1[1] - 1] - date1[2]

        date_to_start = 0
        for i in range(0, date2[1] - 1):
            if i == 1 and self.isLeapYear(date2[0]):
                date_to_end += 29
            else:
                date_to_end += month[i]
        date_to_start += date2[2]

        if date1[0] == date2[0]:
            result = 366 if self.isLeapYear(date1[0]) else 365
            result -= date_to_start + date_to_end
        else:
            result += date_to_start + date_to_end

        return result

# @lc code=end

s = Solution()
print(s.daysBetweenDates("2084-05-19", "1976-02-26"))