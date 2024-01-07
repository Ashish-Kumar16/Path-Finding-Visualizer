import random
import queue
import os

def generate_maze(size, wall_percentage):
    maze = [['◌' for _ in range(size)] for _ in range(size)]

    # Set start and end points
    start = (0, 0)
    end = (size - 1, size - 1)

    maze[start[0]][start[1]] = 'S'
    maze[end[0]][end[1]] = 'E'

    # Calculate the maximum number of walls based on the percentage
    max_walls = int((wall_percentage / 100) * (size * size))

    # Add walls randomly within the limit
    num_walls = 0
    while num_walls < max_walls:
        x, y = random.randint(0, size - 1), random.randint(0, size - 1)
        if (x, y) not in [start, end] and maze[x][y] != '|':
            maze[x][y] = '|'
            num_walls += 1

    return maze, start, end

def print_maze(maze):
    os.system('clear' if os.name == 'posix' else 'cls')  # Clear the terminal screen

    for row in maze:
        print(' '.join(str(cell) for cell in row))
    print()