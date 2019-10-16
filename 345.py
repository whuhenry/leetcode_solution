class Solution:
    def reverseVowels(self, s: str) -> str:
        l = 0
        r = len(s) - 1
        yuanyin = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        ans = list(s)
        while l < r:
            while s[l] not in yuanyin:
                l += 1
                if l >= len(s):
                    break
            while s[r] not in yuanyin:
                r -= 1
                if r < 0:
                    break
            if l >= len(s) or r < 0:
                break
            ans[l] = s[r]
            ans[r] = s[l]
            l += 1
            r -= 1
        return ''.join(ans)

if __name__ == "__main__":
    s = Solution()
    print(s.reverseVowels('.,'))