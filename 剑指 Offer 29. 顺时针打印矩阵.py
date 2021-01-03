class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        limits = [0, n - 1, m - 1, 0]
        limits_delta = [1, -1, -1, 1]
        loc = [0, 0]
        direction = 1
        step = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        result = []
        while limits[0] < limits[2] or limits[3] < limits[1]:
            while limits[0] <= loc[0] <= limits[2] and limits[3] <= loc[1] <= limits[1]:
                result.append(matrix[loc[0]][loc[1]])
                loc[0] += step[direction][0]
                loc[1] += step[direction][1]

            modify_edge = (direction - 1 + 4) % 4
            limits[modify_edge] += limits_delta[modify_edge]
            loc[0] -= step[direction][0]
            loc[1] -= step[direction][1]
            direction = (direction + 1) % 4
            loc[0] += step[direction][0]
            loc[1] += step[direction][1]
        if len(result) < m * n:
            result.append(matrix[loc[0]][loc[1]])

        return result