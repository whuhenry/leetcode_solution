class Solution:
    def masterMind(self, solution: str, guess: str) -> List[int]:
        s_l, g_l = {'R': 0, 'G': 0, 'B': 0, 'Y': 0}, {'R': 0, 'G': 0, 'B': 0, 'Y': 0}
        result = [0, 0]
        for i in range(4):
            if solution[i] == guess[i]:
                result[0] += 1
            else:
                s_l[solution[i]] += 1
                g_l[guess[i]] += 1
        for ch in ['R', 'G', 'B', 'Y']:
            result[1] += min(s_l[ch], g_l[ch])
        return result