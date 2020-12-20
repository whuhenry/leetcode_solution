class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace('-', '')
        number = number.replace(' ', '')
        n = len(number)
        result = []
        idx = 0
        while n - idx >= 3:
            result.append(number[idx: idx + 3])
            idx += 3
        left = n - idx
        if left == 1:
            tmp = result[-1] + number[-1]
            result[-1] = tmp[0: 2]
            result.append(tmp[2: 4])
        elif left == 2:
            result.append(number[idx: idx + 2])
        return '-'.join(result)

s = Solution()
print(s.reformatNumber("--17-5 229 35-39475 "))