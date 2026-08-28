# Rusty No More: Kotlin

This folder is a short-form refresher for Kotlin concepts that commonly appear
in coding interviews. Each exercise is a single function designed to take about
1-3 minutes and no more than 20 lines of implementation. The dynamic programming
exercises allow 3-5 minutes each.

The exercises live in
[`app/src/main/kotlin/Exercises.kt`](app/src/main/kotlin/Exercises.kt). Replace
each `TODO` with your implementation, then run the judge through Gradle to check
it. The exercises are tested with Kotlin 2.4 on JDK 21 and use only the Kotlin
and Java standard libraries.

The Kotlin set follows the same progression and test semantics as the Python
set while using Kotlin conventions: camel-case names, read-only collection
interfaces, nullable return types, `Pair`, data classes, and `ArrayDeque`.

## Topic roadmap

The set contains 60 exercises across these topics:

1. **Collections and iteration** (6) - collection transformations, indexed
   iteration, adjacent values, rotation, flattening, and chunking.
2. **Maps and sets** (5) - membership, frequency maps, grouping, and
   lookup-based pair finding.
3. **Strings** (5) - normalization, run encoding, prefixes, and character
   counts.
4. **Sorting and binary search** (5) - comparators, deterministic ordering,
   bounds, searching, and merging.
5. **Stacks, queues, and priority queues** (5) - bracket matching, postfix
   evaluation, monotonic stacks, bounded queues, and top-k selection.
6. **Two pointers and sliding windows** (5) - paired scans, stable movement,
   fixed windows, and unique-character windows.
7. **Prefix sums and intervals** (5) - range totals, pivot sums, data classes,
   merging, and overlap checks.
8. **Recursion and backtracking** (5) - base cases, recursive traversal,
   binary choices, and subsets.
9. **Linked lists** (5) - nullable traversal, searching, in-place reversal,
   and fast/slow pointers.
10. **Trees** (5) - recursive aggregation, depth-first traversal, and
    breadth-first traversal.
11. **Graphs** (5) - breadth-first search, depth-first search, reachability,
    components, and directed cycles.
12. **Dynamic programming** (4) - one-dimensional transitions, adjacent-state
    choices, reusable coins, and grid paths.

## Project layout

- [`app/src/main/kotlin/Exercises.kt`](app/src/main/kotlin/Exercises.kt) - the 60
  exercises.
- [`app/src/main/kotlin/Judge.kt`](app/src/main/kotlin/Judge.kt) - the test cases
  and command-line judge.
- `app/build.gradle.kts`, `settings.gradle.kts`, `gradle/` - the Gradle build
  that compiles and runs the judge and lets IDEs and language servers import the
  folder.

## Prerequisites

Java is the only requirement; the Gradle wrapper and the Kotlin Gradle plugin
fetch everything else on the first run. Confirm Java is available:

```bash
java -version
```

The build pins the Java toolchain to 21, so Gradle uses a local JDK 21 or
provisions one automatically.

## Run the judge

From this folder, run every available exercise:

```bash
./gradlew -q run
```

Run one or more exercises by function name:

```bash
./gradlew -q run --args="rotateLeft chunkValues"
```

List the exercise names known to the judge:

```bash
./gradlew -q run --args="--list"
```

The first run downloads Gradle and the Kotlin compiler. `-q` hides Gradle's own
output so only the judge is printed; drop it to watch Gradle's progress. The
`run` task propagates the judge's exit status, so the command fails when any
implemented case fails.

Build output goes to `build/` and `app/build/`, which are gitignored. When run
without function names, the judge prints one line for each fully passing
function and details only the failed cases. Exercises that still call `TODO` are
omitted from the per-function output and included in the summary's
skipped-function count. Selecting function names enables detailed output for all
of their cases. The final total counts functions rather than individual test
cases. `PASS`, `FAIL`, and `SKIP` are color-coded in the terminal.

The judge exits with status `0` when every implemented case passes or `1` when
any implemented case fails. It also checks that functions do not mutate inputs
unless an exercise explicitly allows mutation.

## Time estimate

For someone who is comfortable solving a LeetCode medium problem in about 20
minutes, the complete set should take roughly **2.5-3.5 hours**, including
reading the prompts, running the judge, and making small corrections. The
exercises themselves are short, so this works well as two focused sessions.
