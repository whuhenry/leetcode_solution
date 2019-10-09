class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        triangle = [[1]]
        for i in range(1, numRows):
            rows = [1]
            for j in range(1, i):
                rows.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            rows.append(1)
            triangle.append(rows)
        return triangle