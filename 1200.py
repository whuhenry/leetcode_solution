class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        count = len(arr)
        mindif = 1000000
        ans = []
        arr.sort()
        for i in range(count - 1):
                if abs(arr[i] - arr[i + 1]) < mindif:
                    mindif = abs(arr[i] - arr[i + 1])
                    ans.clear()
                    ans.append((arr[i], arr[i + 1]))
                elif abs(arr[i] - arr[i + 1]) == mindif:
                    ans.append((arr[i], arr[i + 1]))
        
        ans.sort()
        return ans