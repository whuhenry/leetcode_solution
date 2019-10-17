class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineCount = [0 for i in range(26)]
        for ch in magazine:
            magazineCount[ord(ch) - ord('a')] += 1
        
        ransomNoteCount = [0 for i in range(26)]
        for ch in ransomNote:
            ransomNoteCount[ord(ch) - ord('a')] += 1
        
        for i in range(26):
            if ransomNoteCount[i] > magazineCount[i]:
                return False
        return True