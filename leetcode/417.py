from collections import deque

class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        num_rows, num_cols = len(heights), len(heights[0])
        dr = [-1, 0, 1, 0]
        dc = [0, -1, 0, 1]

        res = []

        q = deque()
        # BFS from the Pacific and Atlantic edges to find all cells that can reach each ocean
        pacific = [[False] * num_cols for _ in range(num_rows)]
        for i in range(num_cols):
            q.append((0, i))
            pacific[0][i] = True
        for i in range(num_rows):
            q.append((i, 0))
            pacific[i][0] = True
        while q:
            row, col = q.popleft()
            for d in range(4):
                new_row = row + dr[d]
                new_col = col + dc[d]
                within_bounds = new_row >= 0 and new_row < num_rows and new_col >= 0 and new_col < num_cols
                if within_bounds and heights[new_row][new_col] >= heights[row][col] and not pacific[new_row][new_col]:
                    pacific[new_row][new_col] = True
                    q.append((new_row, new_col))
        
        atlantic = [[False] * num_cols for _ in range(num_rows)]
        # BFS from the  Atlantic edges to find all cells that can reach each ocean
        for i in range(num_rows):
            q.append((i, num_cols- 1))
            atlantic[i][num_cols-1] = True
        for i in range(num_cols):
            q.append((num_rows-1, i))
            atlantic[num_rows-1][i] = True
        while q:
            row, col = q.popleft()
            for d in range(4):
                new_row = row + dr[d]
                new_col = col + dc[d]
                within_bounds = new_row >= 0 and new_row < num_rows and new_col >= 0 and new_col < num_cols
                if within_bounds and heights[new_row][new_col] >= heights[row][col] and not atlantic[new_row][new_col]:
                    atlantic[new_row][new_col] = True
                    q.append((new_row, new_col))
        for r in range(num_rows):
            for c in range(num_cols):
                if pacific[r][c] and atlantic[r][c]:
                    res.append([r, c])
        return res
        

def all_cells(m, n):
    return [[r, c] for r in range(m) for c in range(n)]


if __name__ == '__main__':
    s = Solution()
    N = 200
    # height grows left-to-right and top-to-bottom: everything drains to the Pacific,
    # but only the bottom row and right column can reach the Atlantic
    increasing = [[r * N + c for c in range(N)] for r in range(N)]
    decreasing = [[10**5 - (r * N + c) for c in range(N)] for r in range(N)]
    testcases = [
        ([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]],
         [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]),
        ([[1]], [[0, 0]]),
        # a single row or column touches both oceans everywhere
        ([[1, 2, 3, 2, 1]], all_cells(1, 5)),
        ([[5], [1], [5]], all_cells(3, 1)),
        # flat ground: equal heights let water flow anywhere
        ([[7] * 3 for _ in range(3)], all_cells(3, 3)),
        # center pit is trapped
        ([[3, 3, 3], [3, 1, 3], [3, 3, 3]], [c for c in all_cells(3, 3) if c != [1, 1]]),
        # center peak flows down to every edge
        ([[1, 1, 1], [1, 2, 1], [1, 1, 1]], all_cells(3, 3)),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[0, 2], [1, 2], [2, 0], [2, 1], [2, 2]]),
        # top-left cell is a local minimum on the Pacific side only
        ([[1, 2], [4, 3]], [[0, 1], [1, 0], [1, 1]]),
        # bottom-right corner is below its neighbours: it can't reach the Pacific
        ([[10, 10, 10], [10, 10, 10], [10, 10, 0]], [c for c in all_cells(3, 3) if c != [2, 2]]),
        # a tall wall down the middle still touches both oceans at its ends
        ([[1, 5, 1], [1, 5, 1], [1, 5, 1]], all_cells(3, 3)),
        ([[0, 10**5], [10**5, 0]], [[0, 1], [1, 0]]),
        # Max size (200 x 200): checking each cell with its own search is O((mn)^2) and too slow,
        # and recursive DFS can blow past Python's default recursion limit of 1000.
        ([[0] * N for _ in range(N)], all_cells(N, N)),
        (increasing, [[r, c] for r, c in all_cells(N, N) if r == N - 1 or c == N - 1]),
        (decreasing, [[r, c] for r, c in all_cells(N, N) if r == 0 or c == 0]),
    ]
    for i, (heights, want) in enumerate(testcases):
        # any order is accepted, so compare sorted
        got = sorted(s.pacificAtlantic(heights) or [])
        want = sorted(want)
        if got != want:
            if len(want) > 20:
                print('Test {}: got != want, {} cells != {} cells'.format(i, len(got), len(want)))
            else:
                print('Test {}: got != want, {} != {}'.format(i, got, want))
        else:
            print('Test {}: passed'.format(i))
