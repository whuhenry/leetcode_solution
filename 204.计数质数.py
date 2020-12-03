#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#

import math

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        primes_list = []
        for i in range(2, math.ceil(math.sqrt(n)) + 1):
            if not primes_list:
                primes_list.append(i)
            else:
                flag = True
                for prime in primes_list:
                    if prime ** 2 > i:
                        break
                    else:
                        if i % prime == 0:
                            flag = False
                            break
                if flag:
                    primes_list.append(i)

        if not primes_list:
            return 0
        
        result = [0] * n
        result[0] = 1
        result[1] = 1
        for prime in primes_list:
            for i in range(2, (n - 1) // prime + 1):
                result[i * prime] = 1

        return n - sum(result)

# @lc code=end

s = Solution()
print(s.countPrimes(0))
print(s.countPrimes(1))
print(s.countPrimes(2))
print(s.countPrimes(3))
print(s.countPrimes(4))
print(s.countPrimes(10))
print(s.countPrimes(5000000))