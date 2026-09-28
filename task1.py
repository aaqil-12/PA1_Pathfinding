import heapq
import time
import sys


class Node:
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.f < other.f


def manhattan_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def astar(maze, start, end):

    start_time = time.perf_counter()
    nodes_created = 0

    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0

    end_node = Node(None, end)

    nodes_created += 1

    counter = 0
    open_heap = []

    heapq.heappush(
        open_heap,
        (start_node.f, counter, start_node)
    )

    g_scores = {start: 0}
    closed_set = set()

    moves = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    path_found = False
    final_node = None

    while open_heap:

        current_node = heapq.heappop(open_heap)[2]

        if current_node.position in closed_set:
            continue

        closed_set.add(current_node.position)

        if current_node.position == end_node.position:
            path_found = True
            final_node = current_node
            break

        for move in moves:

            row = current_node.position[0] + move[0]
            col = current_node.position[1] + move[1]

            node_position = (row, col)

            if (
                row < 0
                or row >= len(maze)
                or col < 0
                or col >= len(maze[0])
            ):
                continue

            if maze[row][col] == 0:
                continue

            child = Node(current_node, node_position)
            nodes_created += 1

            if child.position in closed_set:
                continue

            move_cost = maze[row][col]
            tentative_g = current_node.g + move_cost

            if (
                child.position in g_scores
                and tentative_g >= g_scores[child.position]
            ):
                continue

            g_scores[child.position] = tentative_g

            child.g = tentative_g
            child.h = manhattan_distance(
                child.position,
                end_node.position
            )
            child.f = child.g + child.h

            counter += 1

            heapq.heappush(
                open_heap,
                (child.f, counter, child)
            )

    end_time = time.perf_counter()
    runtime_ms = (end_time - start_time) * 1000

    if not path_found:

        print("1) Cost of path found : -1")
        print("2) Path sequence      : NULL")
        print(f"3) Total nodes created: {nodes_created}")
        print(f"4) Execution runtime  : {runtime_ms:.4f} ms")

        return None

    path = []

    current = final_node

    while current is not None:
        path.append(current.position)
        current = current.parent

    path.reverse()

    print("A* Search Results")
    print(f"1) Cost of path found : {final_node.g}")
    print(f"2) Path sequence      : {' -> '.join(map(str, path))}")
    print(f"3) Total nodes created: {nodes_created}")
    print(f"4) Execution runtime  : {runtime_ms:.4f} ms")

    return path


def get_map(map_number):

    if map_number == 1:

        maze = [
            [2, 4, 2, 1, 4, 5, 2],
            [0, 1, 2, 3, 5, 3, 1],
            [2, 0, 4, 4, 1, 2, 4],
            [2, 5, 5, 3, 2, 0, 1],
            [4, 3, 3, 2, 1, 0, 1]
        ]

        start = (1, 2)
        end = (4, 3)

    elif map_number == 2:

        maze = [
            [1, 3, 2, 5, 1, 4, 3],
            [2, 1, 3, 1, 3, 2, 5],
            [3, 0, 5, 0, 1, 2, 2],
            [5, 3, 2, 1, 5, 0, 3],
            [2, 4, 1, 0, 0, 2, 0],
            [4, 0, 2, 1, 5, 3, 4],
            [1, 5, 1, 0, 2, 4, 1]
        ]

        start = (3, 6)
        end = (5, 1)

    elif map_number == 3:

        maze = [
            [2, 0, 2, 0, 2, 0, 0, 2, 2, 0],
            [1, 2, 3, 5, 2, 1, 2, 5, 1, 2],
            [2, 0, 2, 2, 1, 2, 1, 2, 4, 2],
            [2, 0, 1, 0, 1, 1, 1, 0, 0, 1],
            [1, 1, 0, 0, 5, 0, 3, 2, 2, 2],
            [2, 2, 2, 2, 1, 0, 1, 2, 1, 0],
            [1, 0, 2, 1, 3, 1, 4, 3, 0, 1],
            [2, 0, 5, 1, 5, 2, 1, 2, 4, 1],
            [1, 2, 2, 2, 0, 2, 0, 1, 1, 0],
            [5, 1, 2, 1, 1, 1, 2, 0, 1, 2]
        ]

        start = (1, 2)
        end = (8, 8)

    elif map_number == 4:

        maze = [
            [1, 2, 3, 1, 2, 4, 1, 3, 2, 1],
            [1, 0, 0, 2, 0, 3, 2, 0, 4, 2],
            [2, 1, 3, 1, 2, 1, 0, 2, 3, 1],
            [3, 0, 2, 0, 4, 2, 1, 3, 0, 2],
            [1, 2, 1, 3, 0, 2, 4, 1, 2, 1],
            [2, 0, 3, 1, 2, 0, 1, 2, 3, 2],
            [1, 3, 2, 4, 1, 2, 3, 0, 1, 1],
            [2, 1, 0, 2, 3, 1, 2, 4, 2, 3],
            [3, 2, 1, 3, 0, 2, 1, 2, 4, 2],
            [1, 1, 2, 1, 3, 2, 1, 1, 2, 1]
        ]

        start = (0, 0)
        end = (9, 9)

    elif map_number == 5:

        maze = [
            [2, 1, 4, 2, 3, 1, 2, 5, 1, 2],
            [1, 0, 2, 0, 1, 3, 0, 2, 4, 1],
            [3, 2, 1, 2, 0, 4, 1, 0, 2, 3],
            [2, 0, 3, 1, 2, 0, 4, 2, 1, 2],
            [1, 3, 0, 2, 5, 1, 2, 3, 0, 1],
            [2, 1, 2, 0, 3, 2, 0, 1, 2, 4],
            [4, 0, 1, 3, 2, 1, 3, 0, 2, 1],
            [1, 2, 3, 1, 0, 2, 4, 1, 3, 2],
            [2, 0, 2, 4, 1, 3, 1, 2, 0, 1],
            [1, 2, 1, 2, 3, 1, 2, 1, 2, 1]
        ]

        start = (9, 0)
        end = (0, 9)

    return maze, start, end


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 task1.py <map 1-5>")
        return

    map_number = int(sys.argv[1])

    if map_number < 1 or map_number > 5:
        print("Map must be between 1 and 5.")
        return

    maze, start, end = get_map(map_number)

    print(f"Map {map_number}")

    astar(
        maze,
        start,
        end
    )


if __name__ == '__main__':
    main()