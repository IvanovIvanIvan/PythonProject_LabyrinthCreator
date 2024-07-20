import random
import copy

def creating_dfs(maze, row, col, visited):
    visited[row][col] = True
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    random.shuffle(directions)
     
    for dr, dc in directions:
        new_row, new_col = row + dr * 2, col + dc * 2
        if (0 <= new_row < len(maze)) and (0 <= new_col < len(maze[0])) and not (visited[new_row][new_col]):
            maze[row + dr][col + dc] = ' '
            maze[new_row][new_col] = ' '
            creating_dfs(maze, new_row, new_col, visited)


def dfs_create_labyrinth(rows, cols):
    maze = [['#' for i in range(cols)] for i in range(rows)]
    visited = [[False for i in range(cols)] for i in range(rows)]
    
    start_row, start_col = random.randrange(1, rows - 1, 2), random.randrange(1, cols - 1, 2)
    maze[start_row][start_col] = ' '
    creating_dfs(maze, start_row, start_col, visited)
    return maze


def solving_dfs(row, col, maze):
    if row < 0 or row >= len(maze) or col < 0 or col >= len(maze[0]) or maze[row][col] != ' ':
        return False
    if (row, col) == (len(maze) - 1, len(maze[0]) - 3) or (row, col) == (len(maze) - 1, len(maze[0]) - 2):
        maze[row][col] = '.'
        return True
    maze[row][col] = '.'
    if solving_dfs(row + 1, col, maze) or solving_dfs(row - 1, col, maze) or solving_dfs(row, col + 1, maze) or solving_dfs(row, col - 1, maze):
        return True
    maze[row][col] = ' '
    return False


def solve_labyrinth(maze):    
    start_row, start_col = 0, 1
    solving_dfs(start_row, start_col, maze)
    for row in maze:
        print(''.join(row))

