# 🌀 Maze Pathfinding with BFS (Python + Curses)

This project is a simple **maze solver** in Python that uses **Breadth-First Search (BFS)** and the **curses library** to animate the pathfinding in the terminal.  

It finds the shortest path from the **start point (`O`)** to the **goal (`X`)** while avoiding walls (`#`).  

---

## 📂 Project Structure

maze_solver.py # main Python script
README.md # this file

yaml
Copier le code

---

## ⚙️ Requirements

- Python 3.7+  
- Libraries:
  - `curses` (built-in on Linux/macOS, but not on Windows)  
  - `queue` (built-in)  
  - `time` (built-in)  

👉 On **Windows**, install the `windows-curses` package first:  
```bash
pip install windows-curses
▶️ How to Run
Clone or download this project.

Run the script in your terminal:

bash
Copier le code
python maze_solver.py
Watch the animation as the program finds the shortest path!

🎮 Controls
The program runs automatically.

When it finishes, press any key to exit.

🗺️ Maze Layout
The maze is defined as a 2D list in the script:

python
Copier le code
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
# → Wall

" " → Empty space (walkable)

O → Start

X → Goal

🧠 Algorithm
Breadth-First Search (BFS) is used to ensure the shortest path is found.

Each step explores neighboring cells (up, down, left, right).

Visited cells are stored to avoid revisiting.

The path is drawn in red while the maze remains in blue.

🎨 Colors
Blue → Maze layout

Red → Path being explored

📸 Demo (Conceptual)
shell
Copier le code
# O # # # # # # #
# . . . # . . . #
# . # . # . # . #
# . # . . . # . #
# . # # # . # . #
# . . . # . # . #
# # # . # . # . #
# . . . . . . . #
# # # # # # # X #
The dots (.) represent the path as it is being animated.
