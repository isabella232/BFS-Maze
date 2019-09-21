import time
import os

def main():
    i = 0
    for file in os.listdir():
        if file.startswith("maze") and file.endswith(".txt"):
            i += 1
            print("Maze", i)
            maze = readMazeFromFile(file)
            start = findStart(maze)
            end = findEnd(maze)

            startTime = time.time()
            path = BFS(maze, start, end)
            endTime = time.time()

            if path == None:
                printMaze(maze)
                print("No path to destination.")
            else:
                printPath(maze, path)
                print("Shortest path: ")
                print(path)

            print("Time taken:", endTime-startTime, "secs")
            print("\n")


# maze: maze to be navigated
# start: starting coordinates (row, col)
# end: ending coordinates (row, col)
# this function should return shortest path start to end
def BFS(maze, start, end):
    # initialize your necessary structures here

    while """insert while condition here""":
        # while loop code
        return


def getAdjacentSpaces(maze, space, visited):
    ''' Returns all legal spaces surrounding the current space
    :param space: tuple containing coordinates (row, col)
    :return: all legal spaces
    '''
    """
    insert your code here
    """
    return None


def findStart(maze):
    """
    :param maze:
    :return: a tuple with start coordinates
    """
    """
    insert your findStart code here
    """
    return None


def findEnd(maze):
    """
    :param maze:
    :return: a tuple with end coordinates
    """
    """
    insert your findEnd code here
    """
    return None


def readMazeFromFile(f):
    maze = list()
    with open(f) as file:
        for line in file:
            maze.append(list(line.rstrip()))
    return maze


def printMaze(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            print(maze[i][j], end="")
        print()


def printPath(maze, path):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if tuple([i, j]) in path and maze[i][j] != 's' and maze[i][j] != 'e':
                print("x", end="")
            else:
                print(maze[i][j], end="")
        print()

main()
