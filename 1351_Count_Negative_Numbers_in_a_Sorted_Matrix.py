from typing import List


# Solution 1, start at the end, loop forwrad untill you hit a positive number
# and go to next row

def countNegatives(grid: List[List[int]]) -> int:
    neg_count = 0
    column_count = len(grid[0])
    for row in grid:
        for i in range(column_count - 1, -1, -1):
            if row[i] < 0:
                neg_count += 1
            else:
                break
    return neg_count

grid1 = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
grid2 = [[3, 2], [1, 0]]
grid3 = [[1, -1], [-1, -1]]
grid4 = [[-1]]
