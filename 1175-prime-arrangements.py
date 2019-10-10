class Solution:
    def isPrime(self, n: int) -> bool:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def numPrimeArrangements(self, n: int) -> int:
        primeCount = 0
        total = 1
        for i in range(2, n + 1):
            if self.isPrime(i):
                primeCount += 1
        for i in range(1, primeCount + 1):
            total = (total * i) % 1000000007
        for i in range(1, n - primeCount + 1):
            total = (total * i) % 1000000007
        return total