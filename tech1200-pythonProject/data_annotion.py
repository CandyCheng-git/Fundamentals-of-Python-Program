from collections import deque

def parse_input(file_path):
    objects = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            obj, x, y = line.strip().split()
            objects.append((obj, int(x), int(y)))
    return objects

def initialize_grid(objects):
    max_x = max(obj[1] for obj in objects)
    max_y = max(obj[2] for obj in objects)
    grid = [[' ' for _ in range(max_y + 1)] for _ in range(max_x + 1)]
    for obj, x, y in objects:
        grid[x][y] = obj
    return grid

def is_connected(grid, x1, y1, x2, y2):
    if 0 <= x2 < len(grid) and 0 <= y2 < len(grid[0]):
        obj1 = grid[x1][y1]
        obj2 = grid[x2][y2]
        if obj1 == '*' or obj2 == '*':
            return True
        # Define connectivity rules for pipes
        # This is a simplified example, actual rules depend on pipe shapes
        connections = {
            '═': [(0, -1), (0, 1)],  # left, right
            '║': [(-1, 0), (1, 0)],  # up, down
            '╔': [(1, 0), (0, 1)],   # down, right
            '╗': [(1, 0), (0, -1)],  # down, left
            '╚': [(0, 1), (-1, 0)],  # up, right
            '╝': [(0, -1), (-1, 0)], # up, left
            '╠': [(-1, 0), (1, 0), (0, 1)],  # up, down, right
            '╣': [(-1, 0), (1, 0), (0, -1)], # up, down, left
            '╦': [(1, 0), (0, -1), (0, 1)],  # down, left, right
            '╩': [(-1, 0), (0, -1), (0, 1)]  # up, left, right
        }
        for dx, dy in connections.get(obj1, []):
            if x1 + dx == x2 and y1 + dy == y2:
                return True
    return False

def bfs(grid, source):
    visited = set()
    queue = deque([source])
    connected_sinks = set()

    while queue:
        x, y = queue.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if is_connected(grid, x, y, nx, ny):
                if grid[nx][ny].isupper():
                    connected_sinks.add(grid[nx][ny])
                queue.append((nx, ny))

    return connected_sinks

def find_connected_sinks(file_path):
    objects = parse_input(file_path)
    grid = initialize_grid(objects)
    source = next((x, y) for obj, x, y in objects if obj == '*')
    connected_sinks = bfs(grid, source)
    return sorted(connected_sinks)

# Example usage
file_path = "C:\\Users\\Candy\\OneDrive\\Work\\DataAnnotation\\coding_qual_input.txt"
print("Result:", find_connected_sinks(file_path))
