class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        fqueries = []
        fwords = []
        for query in queries:
            flags = [0 for i in range(26)]
            for ch in query:
                flags[ord(ch) - ord('a')] += 1
            for i in range(26):
                if flags[i] > 0:
                    fqueries.append(i)
                    break
        
        for word in words:
            flags = [0 for i in range(26)]
            for ch in word:
                flags[ch - 'a'] += 1
            for i in range(26):
                if flags[i] > 0:
                    fwords.append(i)
                    break

        result = []
        for fquery in fqueries:
            count = 0
            for fword in fwords:
                if fquery < fword:
                    count += 1
            result.append(count)
        return result
        
