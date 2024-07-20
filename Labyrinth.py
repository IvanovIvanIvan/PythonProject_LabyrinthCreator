import random
import copy
from mst import mst_create_labyrinth
from dfs import creating_dfs, solving_dfs, dfs_create_labyrinth, solve_labyrinth


class Labyrinth:


    maze = []

    def __init__(self, flag):
        self.flag = flag
        if flag == 0:
            self.rows = random.randrange(21, 51, 2)
            self.cols = random.randrange(21, 51, 2)
            rows = self.rows
            cols = self.cols
            self.maze = dfs_create_labyrinth(rows, cols)
            self.maze[0][1] = ' '
            self.maze[rows-1][cols-2] = ' '
        if flag == 1:
            self.maze = mst_create_labyrinth(9, 9)
            self.rows = len(self.maze)
            self.cols = len(self.maze[0])

    def solve(self):
        solved_maze = copy.deepcopy(self.maze)
        solve_labyrinth(solved_maze)

    def print(self):
        for row in self.maze:
            print(''.join(row))
    def export(self, path):
        output_file = open(path, 'w')
        output_string = ''
        for row in self.maze:
            output_string+=''.join(row)
            output_string+='\n'
        output_file.write(output_string)

    def m_import(self, path):
        input_file = open(path, 'r')
        self.flag = 2
        self.maze = input_file.readlines()
        maze_copy = []
        for i in self.maze:
            copy = []
            for j in i:
                copy.append(j)
            copy.pop()
            maze_copy.append(copy)
        self.maze = maze_copy
        self.cols = len(self.maze)
        self.rows = len(self.maze[0])



