class Solution:
    def dayOfYear(self, date: str) -> int:
        dateSep = date.split('-')
        year = int(dateSep[0])
        month = int(dateSep[1])
        day = int(dateSep[2])
        dayOfMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            dayOfMonth[1] = 29
        dayCount = 0
        for i in range(month - 1):
            dayCount += dayOfMonth[i]
        dayCount += day
        return dayCount