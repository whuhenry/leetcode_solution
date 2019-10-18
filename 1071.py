class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        maxLen = min(len(str1), len(str2))
        ans = ''
        for partCount in range(1, min(len(str1), len(str2)) + 1):
            lenT = maxLen // partCount
            if not (len(str1) % lenT == 0 and len(str2) % lenT == 0):
                continue

            if str1[0: lenT] != str2[0: lenT]:
                continue
            flag = True
            for i in range(len(str1) // lenT):
                if (str1[i * lenT: (i + 1) * lenT] != str1[0: lenT]):
                    flag = False
                    break
            if flag:
                for i in range(len(str2) // lenT):
                    if (str2[i * lenT: (i + 1) * lenT] != str2[0: lenT]):
                        flag = False
                        break
            if flag:
                ans = str1[0: lenT]
                break

        return ans