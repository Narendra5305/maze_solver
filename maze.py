import random
from queue import Queue

RED = '\033[91m'  # Red color
GREEN = '\033[92m'  # Green color
YELLOW = '\033[93m'  # Yellow color
BLUE = '\033[94m'  # Blue color
END_COLOR = '\033[0m'   # Reset color
CYAN = '\033[96m'  # Cyan color
PURPLE = '\033[95m'  # Purple color

# Constants and Colors
WALL = f'{RED}█{END_COLOR}'
START = 'S'
END = 'E'
PATH = f'{GREEN}◉{END_COLOR}'
OPEN_SPACE = f'{BLUE}○{END_COLOR}'

# Maze Generation
def generate_maze(n, wall_percentage):
    maze = [[OPEN_SPACE] * n for _ in range(n)]
    num_walls = int(n * n * wall_percentage/100)
    for _ in range(num_walls):
        row, col = random.randint(0, n - 1), random.randint(0, n - 1)
        maze[row][col] = WALL
    maze[0][0] = START
    maze[n - 1][n - 1] = END

    return maze

# Maze Printing
def print_maze(maze):
    for row in maze:
        print(" ".join(row))

# Path Finding
def find_path(maze):
    start = (0, 0)
    end = (len(maze) - 1, len(maze[0]) - 1)
    visited = set()
    queue = Queue()
    queue.put((start, [start]))
    while not queue.empty():
        current, path = queue.get()

        if current == end:
            return path

        for neighbor in get_neighbors(maze, current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.put((neighbor, path + [neighbor]))

    return None

# Get Neighbors
def get_neighbors(maze, current):
    row, col = current
    neighbors = []
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] != WALL:
            neighbors.append((new_row, new_col))

    return neighbors

# Mark Path
def mark_path(maze, path):
    for row, col in path:
        if maze[row][col] != START and maze[row][col] != END:
            maze[row][col] = PATH

# Main Function
def main():
    while True:
        n = int(input("Enter maze size (n): "))
        wall_percentage = float(input("Enter wall percentage: "))

        if wall_percentage > 25:
            print("Generate value between 0-25")
            continue

        maze = generate_maze(n, wall_percentage)
        print_maze(maze)

        option = input("Choose an option (P: Print Path, G: Generate Another Maze, E: Exit): ").upper()

        if option == 'P':
            path = find_path(maze)

            if path:
                mark_path(maze, path)
                print("Path found")
                print_maze(maze)
                ask_option = input("Generate path else exit: ").upper()
                if ask_option == "G":
                    continue
                elif ask_option == "E":
                    print("Exiting the game.")
                    break
                else:
                    print("Invalid option. Please enter P, G, or E.")
                    break
            else:
                print("No path found")


if __name__ == "__main__":
    main()
