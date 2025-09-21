import curses 
from curses import wrapper
import queue
import time

maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", "#", " ", " ", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", "#", "#", " ", "#", " ", "#"],
    ["#", " ", " ", " ", "#", " ", "#", " ", "#"],
    ["#", "#", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

def print_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i, j*2, "X", RED)  # path in RED
            else:
                stdscr.addstr(i, j*2, value, BLUE)  # maze in BLUE

def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return (i, j)
    return None

def find_path(maze, stdscr):
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)
    q = queue.Queue()
    q.put((start_pos, [start_pos]))
    visited = {start_pos}
    
    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        stdscr.clear()
        print_maze(maze, stdscr, path)
        time.sleep(0.1)  # smoother
        stdscr.refresh()
        
        if maze[row][col] == end:
            return path

        for neighbor in find_neighbors(maze, row, col):
            if neighbor not in visited:
                r, c = neighbor
                if maze[r][c] != "#":
                    q.put((neighbor, path + [neighbor]))
                    visited.add(neighbor)

def find_neighbors(maze, row, col):
    neighbors = []
    if row > 0: neighbors.append((row - 1, col))      # UP
    if row + 1 < len(maze): neighbors.append((row + 1, col))  # DOWN
    if col > 0: neighbors.append((row, col - 1))      # LEFT
    if col + 1 < len(maze[0]): neighbors.append((row, col + 1)) # RIGHT
    return neighbors

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    find_path(maze, stdscr)
    stdscr.getch()

wrapper(main)
