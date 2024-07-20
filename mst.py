import random


def mst_create_labyrinth(rows, cols):


    class Graph:


        def __init__(self, vertices):
            self.vertixes = vertices
            self.graph = []

        def add_edge(self, u, v, w):
            self.graph.append([u, v, w])

        def find_parent(self, parent, vertex):
            if parent[vertex] == vertex:
                return vertex
            return self.find_parent(parent, parent[vertex])

        def union(self, parent, rank, x, y):
            x_root = self.find_parent(parent, x)
            y_root = self.find_parent(parent, y)

            if rank[x_root] < rank[y_root]:
                parent[x_root] = y_root
            elif rank[x_root] > rank[y_root]:
                parent[y_root] = x_root
            else:
                parent[y_root] = x_root
                rank[x_root] += 1

        def kruskal_mst(self):
            result = []
            i, e = 0, 0
            random.shuffle(self.graph)
            parent = []
            rank = []

            for node in range(self.vertixes):
                parent.append(node)
                rank.append(0)

            while e < self.vertixes - 1:
                u, v, w = self.graph[i]
                i += 1
                x = self.find_parent(parent, u)
                y = self.find_parent(parent, v)

                if x != y:
                    e += 1
                    result.append([u, v, w])
                    self.union(parent, rank, x, y)
                    
            return result

    graph = Graph(rows*cols)
    for i in range(rows):
        for j in range(cols):
            if i>0:
                graph.add_edge(i*cols + j, (i-1)*cols+j, 1)
            if i<rows-1:
                graph.add_edge(i*cols + j, (i+1)*cols+j, 1)
            if j>0:
                graph.add_edge(i*cols + j, (i)*cols+j-1, 1)
            if j<cols-1:
                graph.add_edge(i*cols + j, (i)*cols+j+1, 1)
    graph.graph = graph.kruskal_mst()
    maze_output_list = ['#'+' '+'#'*(cols*3-2)+'#']

    for i in range(rows):
        line = '#'
        next_line = ''
        for j in range(cols):
            if ([i*rows+j, i*rows+j+1, 1] in graph.graph) or ([i*rows+j+1, i*rows+j, 1] in graph.graph):
                line+=('   ')
            else:
                line+=(' ##')
            if ([(i+1)*rows+j, i*(rows)+j, 1] in graph.graph) or [i*(rows)+j, (i+1)*rows+j, 1] in graph.graph:
                    next_line+='   '
            else:
                next_line+='###'
        maze_output_list.append(line)
        if '#' in next_line and i!=rows - 1:
            next_line = next_line[0:len(next_line)-1]
            next_line +='#'
            maze_output_list.append('#'+next_line) 
    maze_output_list.append('#'*(cols*3-2)+' '+'#'+'#')
    output = []

    for i in range(len(maze_output_list)):
        output.append([])
        for j in maze_output_list[i]:
            output[i].append(j)

    return output
    