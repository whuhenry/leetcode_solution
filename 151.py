class Solution:
    def reverseWords(self, s: str) -> str:
        strList = s.split()
        strList = strList[::-1]
        result = ''
        if len(strList) == 0:
            return result
        for i in range(len(strList) - 1):
            result += strList[i] + " "
        result += strList[len(strList) - 1]
        return result