import heapq
import time
import random
import sys


class Node:

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


def heuristic_h1(pos1, pos2, maze):
    return 0


def heuristic_h2(pos1, pos2, maze):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def heuristic_h3(pos1, pos2, maze):
    distance = abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    total = 0
    count = 0

    for row in maze:
        for value in row:
            if value != 0:
                total += value
                count += 1

    average_cost = total / count

    return distance * average_cost


def heuristic_h4(pos1, pos2, maze):
    distance = abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    error = random.choice([-3, -2, -1, 1, 2, 3])

    return max(0, distance + error)


def get_heuristic(pos1, pos2, maze, heuristic_number):

    if heuristic_number == 1:
        return heuristic_h1(pos1, pos2, maze)

    elif heuristic_number == 2:
        return heuristic_h2(pos1, pos2, maze)

    elif heuristic_number == 3:
        return heuristic_h3(pos1, pos2, maze)

    elif heuristic_number == 4:
        return heuristic_h4(pos1, pos2, maze)


def astar(maze, start, end, heuristic_number):

    start_time = time.perf_counter()
    nodes_created = 0

    start_node = Node(None, start)
    start_node.g = 0
    start_node.h = 0
    start_node.f = 0

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

    final_node = None

    while open_heap:

        current_node = heapq.heappop(open_heap)[2]

        if current_node.position in closed_set:
            continue

        closed_set.add(current_node.position)

        if current_node.position == end_node.position:
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

            child.h = get_heuristic(
                child.position,
                end_node.position,
                maze,
                heuristic_number
            )

            child.f = child.g + child.h

            counter += 1

            heapq.heappush(
                open_heap,
                (child.f, counter, child)
            )

    end_time = time.perf_counter()

    runtime_ms = (end_time - start_time) * 1000

    if final_node is None:

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
    print(f"Heuristic H{heuristic_number}")
    print(f"1) Cost of path found : {final_node.g}")
    print(f"2) Path sequence      : {' -> '.join(map(str, path))}")
    print(f"3) Total nodes created: {nodes_created}")
    print(f"4) Execution runtime  : {runtime_ms:.4f} ms")

    return path


def main():

    maze = [
        [1, 2, 1, 1, 0, 1, 1],
        [1, 5, 4, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 3, 0, 0, 1],
        [1, 1, 1, 2, 1, 1, 1]
    ]

    start = (0, 0)
    end = (4, 6)

    if len(sys.argv) < 2:
        print("Usage: python task2.py <heuristic 1-4>")
        return

    heuristic_number = int(sys.argv[1])

    if heuristic_number < 1 or heuristic_number > 4:
        print("Heuristic must be between 1 and 4.")
        return

    astar(
        maze,
        start,
        end,
        heuristic_number
    )


if __name__ == '__main__':
    main()