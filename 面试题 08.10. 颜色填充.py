class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        to_fill = [[sr, sc]]
        rows = len(image)
        cols = len(image[0])
        src_color = image[sr][sc]
        if src_color == newColor:
            return image
        neighbors = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        while to_fill:
            new_list = []
            for loc in to_fill:
                image[loc[0]][loc[1]] = newColor
                for neighbor in neighbors:
                    r = loc[0] + neighbor[0]
                    c = loc[1] + neighbor[1]
                    if 0 <= r < rows and 0 <= c < cols and image[r][c] == src_color:
                        new_list.append([r, c])
            to_fill = new_list
        return image