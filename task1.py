import heapq
import time


class Node:
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0  # Cost from start to current node
        self.h = 0  # Heuristic cost from current node to end
        self.f = 0  # Total estimated cost (g + h)

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        # Needed for heapq comparisons when f-scores are equal
        return self.f < other.f


def manhattan_distance(pos1, pos2):
    """Calculates Manhattan distance heuristic between two (row, col) tuples"""
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def astar(maze, start, end):
    """
    Finds path with minimum total move cost using A* pathfinding.

    Maze values: 0 = Impassable, 1-5 = Movement cost into square.
    """

    start_time = time.perf_counter()
    nodes_created = 0

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)

    nodes_created += 1  # Count start_node creation

    # Initialize open priority queue and closed dictionary
    # Open entry format: (f_score, unique_counter, node)
    counter = 0
    open_heap = []
    heapq.heappush(open_heap, (start_node.f, counter, start_node))

    # Track lowest g score seen for each coordinate to avoid redundant work
    g_scores = {start: 0}
    closed_set = set()

    # Define 4-directional moves: Up, Down, Left, Right
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    path_found = False
    final_node = None

    while open_heap:
        current_node = heapq.heappop(open_heap)[2]

        if current_node.position in closed_set:
            continue

        closed_set.add(current_node.position)

        # Found the goal
        if current_node.position == end_node.position:
            path_found = True
            final_node = current_node
            break

        # Generate children (adjacent cells)
        for move in moves:
            row = current_node.position[0] + move[0]
            col = current_node.position[1] + move[1]
            node_position = (row, col)

            # Ensure position is within grid boundaries
            if row < 0 or row >= len(maze) or col < 0 or col >= len(maze[0]):
                continue

            # Ensure walkable terrain (0 is impassable)
            if maze[row][col] == 0:
                continue

            # Create child node and increment node counter
            child = Node(current_node, node_position)
            nodes_created += 1

            if child.position in closed_set:
                continue

            # Calculate movement cost into the target square
            move_cost = maze[row][col]
            tentative_g = current_node.g + move_cost

            # Check if this path to child is better than any previously recorded path
            if child.position in g_scores and tentative_g >= g_scores[child.position]:
                continue

            g_scores[child.position] = tentative_g
            child.g = tentative_g
            child.h = manhattan_distance(child.position, end_node.position)
            child.f = child.g + child.h

            counter += 1
            heapq.heappush(open_heap, (child.f, counter, child))

    end_time = time.perf_counter()
    runtime_ms = (end_time - start_time) * 1000

    if not path_found:
        print("No path found.")
        print(f"Nodes Created: {nodes_created}")
        print(f"Runtime: {runtime_ms:.4f} ms")
        return None

    # Reconstruct path and path cost
    path = []
    curr = final_node

    while curr is not None:
        path.append(curr.position)
        curr = curr.parent

    path = path[::-1]

    # Display results
    print("A* Search Results")
    print(f"1) Cost of path found : {final_node.g}")

    # Source Code

    print(f"2) Path sequence      : {' -> '.join(map(str, path))}")
    print(f"3) Total nodes created: {nodes_created}")
    print(f"4) Execution runtime  : {runtime_ms:.4f} ms")

    return path


def main():
    # Sample maze map: 0 = Impassable, 1-5 = Move costs
    maze = [
        [1, 2, 1, 1, 0, 1, 1],
        [1, 5, 4, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 3, 0, 0, 1],
        [1, 1, 1, 2, 1, 1, 1]
    ]

    start = (0, 0)
    end = (4, 6)

    astar(maze, start, end)


if __name__ == '__main__':
    main()