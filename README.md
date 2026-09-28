# PA1 Pathfinding

This repository contains Task 1 and Task 2 for the A* Pathfinding assignment.

## Clone the Repository

Open a terminal and run:

```bash
git clone https://github.com/aaqil-12/PA1_Pathfinding.git
cd PA1_Pathfinding
```

## Run Task 1

Task 1 uses the Manhattan distance heuristic.

The command format is:

```bash
python3 task1.py <map_number>
```

The map number can be from `1` to `5`.

Run all five maps using:

```bash
python3 task1.py 1
python3 task1.py 2
python3 task1.py 3
python3 task1.py 4
python3 task1.py 5
```

## Run Task 2

Task 2 takes two command-line parameters.

The command format is:

```bash
python3 task2.py <map_number> <heuristic_number>
```

The first number specifies the map:

- `1` = Map 1
- `2` = Map 2
- `3` = Map 3
- `4` = Map 4
- `5` = Map 5

The second number specifies the heuristic:

- `1` = H1: Zero heuristic
- `2` = H2: Manhattan distance
- `3` = H3: Modified Manhattan heuristic
- `4` = H4: Manhattan distance with random error

## Run All Task 2 Combinations

```bash
python3 task2.py 1 1
python3 task2.py 1 2
python3 task2.py 1 3
python3 task2.py 1 4

python3 task2.py 2 1
python3 task2.py 2 2
python3 task2.py 2 3
python3 task2.py 2 4

python3 task2.py 3 1
python3 task2.py 3 2
python3 task2.py 3 3
python3 task2.py 3 4

python3 task2.py 4 1
python3 task2.py 4 2
python3 task2.py 4 3
python3 task2.py 4 4

python3 task2.py 5 1
python3 task2.py 5 2
python3 task2.py 5 3
python3 task2.py 5 4
```

For example:

```bash
python3 task2.py 5 3
```

runs Map 5 using Heuristic H3.

## Program Output

Each run prints:

```text
1) Cost of path found
2) Path sequence
3) Total nodes created
4) Execution runtime
```

If no path is found, the output includes:

```text
1) Cost of path found : -1
2) Path sequence      : NULL
```

## Python Version

The programs should be run using Python 3.

For example:

```bash
python3 task1.py 1
python3 task2.py 1 2
```

If `python3` does not work on your system, try:

```bash
python task1.py 1
python task2.py 1 2
```

## Files

```text
PA1_Pathfinding/
├── task1.py
├── task2.py
└── README.md
```