class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0 for i in range(num_people)]
        idx = 0
        count = 1
        while candies > 0:
            ans[idx] += min(count, candies)
            candies = max(0, candies - count)
            count += 1
            idx = (idx + 1) % num_people
        return ans