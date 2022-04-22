class Solution:
    def reverseBits(self, num: int) -> int:
        tmp = num & 0xffffffff
        a = bin(tmp)
        n = 1

        def max_1_len(n: int):
            return max(map(len, bin(n)[2: ].split('0')))

        result = max_1_len(tmp)
        result = max(result, max_1_len(tmp ^ n))
        for i in range(31):
            n = n << 1
            result = max(result, max_1_len(tmp ^ n))
        
        return result

s = Solution()
print(s.reverseBits(-1))