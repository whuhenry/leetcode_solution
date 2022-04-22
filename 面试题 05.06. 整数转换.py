class Solution:
    def convertInteger(self, A: int, B: int) -> int:
        def to_bits(n):
            result = [0] * 32
            if n < 0:
                result[31] = 1
            tmp = abs(n)
            idx = 0
            while tmp > 0:
                result[idx] = tmp % 2
                tmp = tmp >> 1
                idx += 1
            idx = 0
            if n < 0:
                for i in range(31):
                    result[i] = (result[i] + 1) % 2
                result[0] += 1
                while result[idx] > 1:
                    result[idx + 1] += 1
                    result[idx] = result[idx] % 2
                    idx += 1
            return result
        
        bits_A = to_bits(A)
        bits_B = to_bits(B)
        diff = 0
        for i in range(32):
            if bits_A[i] != bits_B[i]:
                diff += 1
        return diff

s = Solution()
print(s.convertInteger(528611498, -1619967984))