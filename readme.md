## Проект генератор лабиринтов

### Описание:

В рамках проекта реализовано приложение, генерирующее лабиринты двумя способами: с помощью поиска в глубину (dfs) и минимального остовного дерева (mst). Вариант генерации выбирается с помощью аргумента командной строки. Возможен вывод лабиринта в консоль с помощью символов '#' и ' '. Таже возможен экспорт лабиринта подобного формата из текстового файла, и импорт в текстовый файл. Также приложение умеет находить правильный путь в лабиринте и помечать его символом '.' .

### Реализуемый функционал:

Проект запускается с аргументом 0 или 1.

 0 означает генерацию случайного лабиринта с помощью dfs. Гарантируется, что у него существует решение, а его измерения находятся в пределах от 21 до 49.
 
 1 означает генерацию случайного лабиринта с помощью минимального остовного дерева. Гарантируется, что у него имеется решение и его измерения не превышают 27.

Реализованы следующие команды:

**print** - выводит лабиринт в консоль, помечая границы и стены символом '#'

**import** - считывает лабиринт из файла. В данном файле стены лабиринта могут обозначаться любыми символами кроме пробела и точки.

**export** - записывает лабиринт в текстовый файл

**solve** - выводит решённый лабиринт

**stop** - выходит из программы

###  Архитектура:

#### В модуле dfs реализованы следующие функции:

**creating_dfs(maze, row, col, visited)** - рекурсивная функция, которая принимает лабиринт в виде двумерного списка, координаты row, col (номер строки и столбца), а также массив уже посещённых клеток visited и строит лабиринт поиском в глубину.

**dfs_create_labyrinth(rows, cols)** - принимает на вход парметры rows, cols лабиринта (количество его строк и столбцов) и по ним с помощью функции creating_dfs строит случайный лабиринт, где стены помечены символами '#'.

**solving_dfs(row, col, maze)** - рекурсивная функция, принимающая на вход решаемый лабиринт и координаты, которая точками помечает искомый путь от входа до выхода.

**solve_labyrinth(maze)** - функция, которая принимает на вход лабиринт, решает его с помощью функции solving_dfs и выводит его в консоль.

#### В модуле mst реализована следующая функция:

**mst_create_labyrinth(rows, cols)** - принимает на вход параметры лабиринта и строит его, находя случайное минимальное остовное дерево, используя алгоритм крускала.
В данной функции реализован вспомогательный  класс Graph, у которого есть поля vertixes - количество вершин и graph - сам граф в виде списка рёбер. Конструктор класса строит граф без рёбер по данному количеству вершин. Реализованы следующие методы:

**add_edge(self, u, v, w)** - добавляет в граф ребро с вершинами u и v и весом w.

**find_parent(self, parent, vertex)** - находит представителя данной данной компоненты связности в минимальном остовном дереве.

**union(self, parent, rank, x, y)** - объединяет два дерева с вершинами x и y в одно

**kruskal_mst(list)** - пользуясь предыдущими вспомогательными функциями находит минимальное остовное дерево.


#### В модуле Labyrinth реализован класс Labyrinth

Его атрибуты: rows, cols - количество строк и столбцов соответственно, flag - целочисленная переменная, показывающая, каким способом был получен лабиринт и maze - двумерный список, содержащий клетки лабиринта.

Его конструктор принимает на вход переменную flag, которая определяет метод построения лабиринта: 0 - dfs, 1 - минимальное остовное дерево. 

Также реализованы следующие методы:

**print(self)** - выводит лабиринт в консоль

**solve(self)** - решает лабиринт и выводит его в консоль

**export(self, path)** - экспортирует лабиринт в файл по адресу path.

**m_import(self, path)** - импортирует лабиринт из файла по адресу path.






