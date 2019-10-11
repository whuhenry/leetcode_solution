class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        flags = [0 for i in range(26)]
        result = 0
        for ch in chars:
            flags[ord(ch) - ord('a')] += 1
        for word in words:
            countCh = [0 for i in range(26)]
            for ch in word:
                countCh[ord(ch) - ord('a')] += 1
            valid = True
            for i in range(26):
                if countCh[i] > flags[i]:
                    valid = False
                    break
            if valid:
                result += len(word)
        return result