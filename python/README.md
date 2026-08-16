# Rusty No More: Python

This folder is a short-form refresher for Python concepts that commonly appear
in coding interviews. Each exercise is a single function designed to take about
1-3 minutes and no more than 20 lines of implementation. The dynamic programming
exercises allow 3-5 minutes each.

The exercises live in [`exercises.py`](exercises.py). Replace each
`NotImplementedError` with your implementation, then use [`judge.py`](judge.py)
to check it. The exercises target Python 3.14 and use only the standard library.

Exercises designed by [`gpt-5.6-sol`](https://developers.openai.com/api/docs/models/gpt-5.6-sol) with `high` reasoning effort.

## Topic roadmap

The set contains 60 exercises across these topics:

1. **Sequences and iteration** (6) - comprehensions, `enumerate`, `zip`,
   slicing, rotation, flattening, and chunking.
2. **Dictionaries and sets** (5) - membership, frequency maps, grouping, and
   lookup-based pair finding.
3. **Strings** (5) - normalization, run encoding, prefixes, and character
   counts.
4. **Sorting and binary search** (5) - custom keys, deterministic ordering,
   bounds, searching, and merging.
5. **Stacks, queues, and heaps** (5) - bracket matching, postfix evaluation,
   monotonic stacks, bounded queues, and top-k selection.
6. **Two pointers and sliding windows** (5) - paired scans, stable movement,
   fixed windows, and unique-character windows.
7. **Prefix sums and intervals** (5) - range totals, pivot sums, merging, and
   overlap checks.
8. **Recursion and backtracking** (5) - base cases, recursive traversal,
   binary choices, and subsets.
9. **Linked lists** (5) - traversal, searching, reversal, and fast/slow
   pointers.
10. **Trees** (5) - recursive aggregation, depth-first traversal, and
    breadth-first traversal.
11. **Graphs** (5) - breadth-first search, depth-first search, reachability,
    components, and directed cycles.
12. **Dynamic programming** (4) - one-dimensional transitions, adjacent-state
    choices, reusable coins, and grid paths.

## Run the judge

From this folder, run every available exercise:

```bash
python3 judge.py
```

Run one or more exercises by function name:

```bash
python3 judge.py rotate_left chunk_values
```

List the exercise names known to the judge:

```bash
python3 judge.py --list
```

When run without function names, the judge prints one line for each fully
passing function and details only the failed cases. Exercises that raise
`NotImplementedError` are omitted from the per-function output and included in
the summary's skipped-function count. Selecting function names enables detailed
output for all of their cases. The final total counts functions rather than
individual test cases. `PASS`, `FAIL`, and `SKIP` are color-coded in the terminal.

The judge exits with status `0` when every implemented case passes or `1` when
any implemented case fails.

## Time estimate

For someone who is comfortable solving a LeetCode medium problem in about 20
minutes, the complete set should take roughly **2.5-3.5 hours**,
including reading the prompts, running the judge, and making small corrections.
The exercises themselves are short, so this works well as two focused sessions.
