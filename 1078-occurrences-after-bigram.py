class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        textSep = text.split(' ')
        ans = []
        for i in range(len(textSep) - 2):
            if textSep[i] == first and textSep[i + 1] == second:
                ans.append(textSep[i + 2])
        return ans