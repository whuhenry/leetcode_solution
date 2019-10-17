class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        maxlen = max(len(num1), len(num2))
        ans = [0 for i in range(maxlen + 1)]
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(maxlen):
            if i >= len(num1):
                ans[i] = int(num2[i])
            elif i >= len(num2):
                ans[i] = int(num1[i])
            else:
                ans[i] = int(num1[i]) + int(num2[i])
        for i in range(maxlen):
            if ans[i] > 9:
                ans[i + 1] += 1
                ans[i] -= 10
        if ans[maxlen] == 0:
            ans = ans[0: maxlen]
        ansch = [str(i) for i in ans]
        return ''.join(ansch[::-1])