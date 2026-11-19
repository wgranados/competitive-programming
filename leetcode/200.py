from typing import List
import sys
sys.setrecursionlimit(200_000)



class Solution:
    def floodfill(self, row, col, grid):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return 0
        if self.visited[row][col] or grid[row][col] == '0':
            return 0
        self.visited[row][col] = True
        return 1 + self.floodfill(row + 1, col, grid) + self.floodfill(row - 1, col, grid) + self.floodfill(row, col+1, grid) + self.floodfill(row, col-1, grid)
    def numIslands(self, grid: List[List[str]]) -> int:
        self.visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                has_island = True if self.floodfill(row, col, grid) > 0 else False
                if has_island:
                    islands += 1
        return islands


if __name__ == '__main__':
    # Each grid is written as a list of row strings and expanded to
    # List[List[str]] before being passed in.
    testcases = [
        (["11110",
          "11010",
          "11000",
          "00000"], 1),
        (["11000",
          "11000",
          "00100",
          "00011"], 3),
        (["1"], 1),
        (["0"], 0),
        (["101"], 2),
        (["1",
          "0",
          "1"], 2),
        (["10",
          "01"], 2),
        (["111",
          "111"], 1),
        (["000",
          "000"], 0),
        (["101",
          "010",
          "101"], 5),
        (["111",
          "101",
          "111"], 1),
        (["101",
          "101",
          "111"], 1),
        (["11111",
          "00001",
          "11101",
          "10001",
          "11111"], 1),
        # Max size, all land: a recursive DFS will hit the recursion limit here.
        (["1" * 300 for _ in range(300)], 1),
        # Max size, checkerboard: the most islands possible.
        (["".join("1" if (r + c) % 2 == 0 else "0" for c in range(300)) for r in range(300)], 45000),
    ]
    for i, (rows, want) in enumerate(testcases):
        s = Solution()
        got = s.numIslands([list(row) for row in rows])
        if got != want:
            print('Test {}: got != want, {} != {}'.format(i, got, want))
        else:
            print('Test {}: passed'.format(i))
