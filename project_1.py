import argparse
import random
import copy
import Labyrinth

parser = argparse.ArgumentParser()
parser.add_argument('flag')
flag = parser.parse_args()
flag = flag.flag
command = ''
labyrinth = Labyrinth.Labyrinth(int(flag))

while command!='stop':

    command = input()

    if command =='print':
        print('Labyrinth:')
        labyrinth.print()
        print('\n')

    if command == 'import':
        print('Please, write a path of your labyrinth')
        path = str(input())
        labyrinth.m_import(path)

    if command == 'export':
        print('Please, write a path to store your labyrinth')
        path = str(input())
        labyrinth.export(path)

    if command == 'solve':
        print('Solved version of the labyrinth:')
        labyrinth.solve()
        print('\n')
        
