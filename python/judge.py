"""Command-line judge for the Python interview exercises."""

from __future__ import annotations

import argparse
from collections.abc import Callable, Sequence
from copy import deepcopy
from dataclasses import dataclass
from enum import Enum
from typing import Any

import exercises


@dataclass(frozen=True)
class TestCase:
    name: str
    arguments: tuple[Any, ...]
    expected: Any
    allows_mutation: bool = False


@dataclass(frozen=True)
class ExerciseTests:
    name: str
    function: Callable[..., Any]
    cases: tuple[TestCase, ...]


class CaseStatus(Enum):
    PASSED = ("PASS", "\033[32m")
    FAILED = ("FAIL", "\033[31m")
    SKIPPED = ("SKIP", "\033[33m")

    def __init__(self, label: str, color: str) -> None:
        self._label = label
        self._color = color

    @property
    def colored_label(self) -> str:
        return f"{self._color}{self._label}\033[0m"


def _linked_list(values: list[int]) -> exercises.ListNode | None:
    return exercises.ListNode.from_values(values)


def _tree(values: list[int | None]) -> exercises.TreeNode | None:
    return exercises.TreeNode.from_level_order(values)


EXERCISE_TESTS = (
    ExerciseTests(
        "select_even_squares",
        exercises.select_even_squares,
        (
            TestCase("mixed values", ([1, 2, 4, 5],), [4, 16]),
            TestCase("empty input", ([],), []),
            TestCase("negative values and zero", ([-2, -1, 0, 6],), [4, 0, 36]),
        ),
    ),
    ExerciseTests(
        "indexed_characters",
        exercises.indexed_characters,
        (
            TestCase("short word", ("cat",), [(0, "c"), (1, "a"), (2, "t")]),
            TestCase("empty text", ("",), []),
            TestCase("space is retained", ("a a",), [(0, "a"), (1, " "), (2, "a")]),
        ),
    ),
    ExerciseTests(
        "adjacent_sums",
        exercises.adjacent_sums,
        (
            TestCase("three values", ([1, 4, -2],), [5, 2]),
            TestCase("single value", ([7],), []),
            TestCase("negative pair", ([-3, -5],), [-8]),
        ),
    ),
    ExerciseTests(
        "rotate_left",
        exercises.rotate_left,
        (
            TestCase("single step", ([1, 2, 3, 4], 1), [2, 3, 4, 1]),
            TestCase("steps exceed length", ([1, 2, 3, 4], 6), [3, 4, 1, 2]),
            TestCase("empty input", ([], 99), []),
            TestCase("zero steps", ([1, 2], 0), [1, 2]),
        ),
    ),
    ExerciseTests(
        "flatten_once",
        exercises.flatten_once,
        (
            TestCase("empty group included", ([[1, 2], [], [3]],), [1, 2, 3]),
            TestCase("no groups", ([],), []),
            TestCase("only empty groups", ([[], []],), []),
        ),
    ),
    ExerciseTests(
        "chunk_values",
        exercises.chunk_values,
        (
            TestCase("partial final chunk", ([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]]),
            TestCase("empty input", ([], 3), []),
            TestCase("chunk larger than input", ([1, 2], 5), [[1, 2]]),
            TestCase("unit chunks", ([3, 4], 1), [[3], [4]]),
        ),
    ),
) + (
    ExerciseTests(
        "frequency_map",
        exercises.frequency_map,
        (
            TestCase("repeated values", (["a", "b", "a"],), {"a": 2, "b": 1}),
            TestCase("empty input", ([],), {}),
            TestCase("one distinct value", (["x", "x", "x"],), {"x": 3}),
        ),
    ),
    ExerciseTests(
        "first_unique_value",
        exercises.first_unique_value,
        (
            TestCase("unique value after repeats", ([4, 2, 4, 3, 2],), 3),
            TestCase("no unique value", ([1, 1, 2, 2],), None),
            TestCase("single value", ([9],), 9),
        ),
    ),
    ExerciseTests(
        "group_indices",
        exercises.group_indices,
        (
            TestCase(
                "repeated values",
                (["a", "b", "a"],),
                {"a": [0, 2], "b": [1]},
            ),
            TestCase("empty input", ([],), {}),
            TestCase("one group", (["x", "x"],), {"x": [0, 1]}),
        ),
    ),
    ExerciseTests(
        "common_values",
        exercises.common_values,
        (
            TestCase("duplicates collapse", ([1, 2, 2], [2, 3]), {2}),
            TestCase("disjoint inputs", ([1], [2]), set()),
            TestCase("negative values", ([-1, 0, 2], [2, -1]), {-1, 2}),
        ),
    ),
    ExerciseTests(
        "two_sum_indices",
        exercises.two_sum_indices,
        (
            TestCase("pair at beginning", ([2, 7, 11], 9), (0, 1)),
            TestCase("pair later in input", ([3, 2, 4], 6), (1, 2)),
            TestCase("no pair", ([1, 2, 3], 99), None),
        ),
    ),
    ExerciseTests(
        "normalize_words",
        exercises.normalize_words,
        (
            TestCase("mixed case and spaces", ("  Hello  WORLD ",), ["hello", "world"]),
            TestCase("all whitespace", (" \t\n",), []),
            TestCase("punctuation retained", ("Hi, THERE!",), ["hi,", "there!"]),
        ),
    ),
    ExerciseTests(
        "is_normalized_palindrome",
        exercises.is_normalized_palindrome,
        (
            TestCase("phrase palindrome", ("A man, a plan, a canal: Panama!",), True),
            TestCase("not a palindrome", ("race a car",), False),
            TestCase("no alphanumeric characters", ("! ?",), True),
        ),
    ),
    ExerciseTests(
        "run_length_encode",
        exercises.run_length_encode,
        (
            TestCase("several runs", ("aaabbc",), "a3b2c1"),
            TestCase("empty text", ("",), ""),
            TestCase("single character", ("z",), "z1"),
        ),
    ),
    ExerciseTests(
        "longest_common_prefix",
        exercises.longest_common_prefix,
        (
            TestCase("shared prefix", (["flower", "flow", "flight"],), "fl"),
            TestCase("no words", ([],), ""),
            TestCase("no shared prefix", (["dog", "racecar", "car"],), ""),
            TestCase("single word", (["solo"],), "solo"),
        ),
    ),
    ExerciseTests(
        "are_anagrams",
        exercises.are_anagrams,
        (
            TestCase("same counts", ("listen", "silent"), True),
            TestCase("different counts", ("rat", "car"), False),
            TestCase("spaces count", ("a b", "ab "), True),
            TestCase("case sensitive", ("A", "a"), False),
        ),
    ),
    ExerciseTests(
        "sort_by_length",
        exercises.sort_by_length,
        (
            TestCase("different lengths", (["pear", "fig", "apple"],), ["fig", "pear", "apple"]),
            TestCase("alphabetical tie", (["dog", "ant", "cat"],), ["ant", "cat", "dog"]),
            TestCase("empty input", ([],), []),
        ),
    ),
    ExerciseTests(
        "top_k_frequent",
        exercises.top_k_frequent,
        (
            TestCase("frequency order", ([1, 1, 2, 2, 3], 2), [1, 2]),
            TestCase("numeric tie break", ([3, 1, 2], 2), [1, 2]),
            TestCase("zero requested", ([1, 1], 0), []),
        ),
    ),
    ExerciseTests(
        "binary_search",
        exercises.binary_search,
        (
            TestCase("target present", ([1, 4, 7, 9], 7), 2),
            TestCase("target absent", ([1, 4, 7, 9], 5), -1),
            TestCase("empty input", ([], 3), -1),
            TestCase("first value", ([2, 5], 2), 0),
        ),
    ),
    ExerciseTests(
        "lower_bound",
        exercises.lower_bound,
        (
            TestCase("duplicate target", ([1, 3, 3, 5], 3), 1),
            TestCase("insert at end", ([1, 3, 5], 7), 3),
            TestCase("insert at beginning", ([2, 4], 1), 0),
            TestCase("empty input", ([], 8), 0),
        ),
    ),
    ExerciseTests(
        "merge_sorted",
        exercises.merge_sorted,
        (
            TestCase("interleaved values", ([1, 4], [2, 2, 5]), [1, 2, 2, 4, 5]),
            TestCase("one empty input", ([], [1, 3]), [1, 3]),
            TestCase("duplicates from both", ([1, 2], [1, 2]), [1, 1, 2, 2]),
        ),
    ),
    ExerciseTests(
        "has_balanced_brackets",
        exercises.has_balanced_brackets,
        (
            TestCase("nested brackets", ("([]{})",), True),
            TestCase("crossed brackets", ("([)]",), False),
            TestCase("missing closer", ("(()",), False),
            TestCase("empty text", ("",), True),
        ),
    ),
    ExerciseTests(
        "evaluate_postfix",
        exercises.evaluate_postfix,
        (
            TestCase("multiple operations", (["2", "3", "+", "4", "*"],), 20),
            TestCase("operand order", (["5", "2", "-"],), 3),
            TestCase("negative integer", (["-3", "2", "*"],), -6),
        ),
    ),
    ExerciseTests(
        "next_greater_values",
        exercises.next_greater_values,
        (
            TestCase("mixed values", ([2, 1, 3],), [3, 3, -1]),
            TestCase("descending values", ([3, 2, 1],), [-1, -1, -1]),
            TestCase("equal values", ([2, 2, 3],), [3, 3, -1]),
            TestCase("empty input", ([],), []),
        ),
    ),
    ExerciseTests(
        "last_k_items",
        exercises.last_k_items,
        (
            TestCase("discard older values", ([1, 2, 3, 4], 2), [3, 4]),
            TestCase("empty input", ([], 3), []),
            TestCase("limit exceeds length", ([1, 2], 5), [1, 2]),
        ),
    ),
    ExerciseTests(
        "k_largest",
        exercises.k_largest,
        (
            TestCase("duplicates retained", ([3, 1, 4, 4], 2), [4, 4]),
            TestCase("zero requested", ([1, 2], 0), []),
            TestCase("negative values", ([-4, -1, -3], 2), [-1, -3]),
        ),
    ),
    ExerciseTests(
        "has_pair_with_sum",
        exercises.has_pair_with_sum,
        (
            TestCase("pair exists", ([1, 2, 4, 7], 9), True),
            TestCase("pair absent", ([1, 2, 4, 7], 20), False),
            TestCase("equal values at different positions", ([3, 3], 6), True),
            TestCase("one value cannot pair with itself", ([3], 6), False),
        ),
    ),
    ExerciseTests(
        "deduplicate_sorted",
        exercises.deduplicate_sorted,
        (
            TestCase("several duplicates", ([1, 1, 2, 2, 3],), [1, 2, 3]),
            TestCase("empty input", ([],), []),
            TestCase("already distinct", ([-1, 0, 2],), [-1, 0, 2]),
        ),
    ),
    ExerciseTests(
        "move_zeroes_to_end",
        exercises.move_zeroes_to_end,
        (
            TestCase("interspersed zeroes", ([0, 1, 0, 3],), [1, 3, 0, 0]),
            TestCase("no zeroes", ([1, 2],), [1, 2]),
            TestCase("only zeroes", ([0, 0],), [0, 0]),
        ),
    ),
    ExerciseTests(
        "maximum_window_sum",
        exercises.maximum_window_sum,
        (
            TestCase("best final window", ([1, 4, 2, 10], 2), 12),
            TestCase("negative values", ([-2, -1, -3], 2), -3),
            TestCase("window is full input", ([1, 2], 2), 3),
        ),
    ),
    ExerciseTests(
        "longest_unique_substring_length",
        exercises.longest_unique_substring_length,
        (
            TestCase("repeated sequence", ("abcabcbb",), 3),
            TestCase("empty text", ("",), 0),
            TestCase("one repeated character", ("bbbbb",), 1),
            TestCase("overlapping window", ("pwwkew",), 3),
        ),
    ),
    ExerciseTests(
        "build_prefix_sums",
        exercises.build_prefix_sums,
        (
            TestCase("mixed signs", ([2, -1, 3],), [0, 2, 1, 4]),
            TestCase("empty input", ([],), [0]),
            TestCase("negative total", ([-2, -3],), [0, -2, -5]),
        ),
    ),
    ExerciseTests(
        "range_sum",
        exercises.range_sum,
        (
            TestCase("middle range", ([0, 2, 1, 4], 1, 3), 2),
            TestCase("entire range", ([0, 2, 1, 4], 0, 3), 4),
            TestCase("empty range", ([0, 2, 1, 4], 2, 2), 0),
        ),
    ),
    ExerciseTests(
        "pivot_index",
        exercises.pivot_index,
        (
            TestCase("middle pivot", ([1, 7, 3, 6, 5, 6],), 3),
            TestCase("no pivot", ([1, 2, 3],), -1),
            TestCase("single value", ([0],), 0),
            TestCase("first index pivot", ([2, 1, -1],), 0),
        ),
    ),
    ExerciseTests(
        "merge_intervals",
        exercises.merge_intervals,
        (
            TestCase("overlapping intervals", ([(1, 3), (2, 4), (7, 8)],), [(1, 4), (7, 8)]),
            TestCase("unsorted disjoint intervals", ([(5, 6), (1, 2)],), [(1, 2), (5, 6)]),
            TestCase("touching endpoints", ([(1, 3), (3, 5)],), [(1, 5)]),
            TestCase("empty input", ([],), []),
        ),
    ),
    ExerciseTests(
        "intervals_overlap",
        exercises.intervals_overlap,
        (
            TestCase("touching endpoints", ((1, 3), (3, 5)), True),
            TestCase("separate intervals", ((1, 2), (3, 4)), False),
            TestCase("contained interval", ((1, 8), (3, 4)), True),
        ),
    ),
    ExerciseTests(
        "factorial_recursive",
        exercises.factorial_recursive,
        (
            TestCase("zero", (0,), 1),
            TestCase("one", (1,), 1),
            TestCase("positive value", (5,), 120),
        ),
    ),
    ExerciseTests(
        "recursive_sum",
        exercises.recursive_sum,
        (
            TestCase("mixed signs", ([2, -1, 4],), 5),
            TestCase("empty input", ([],), 0),
            TestCase("single value", ([7],), 7),
        ),
    ),
    ExerciseTests(
        "reverse_text_recursive",
        exercises.reverse_text_recursive,
        (
            TestCase("word", ("code",), "edoc"),
            TestCase("empty text", ("",), ""),
            TestCase("palindrome", ("level",), "level"),
        ),
    ),
    ExerciseTests(
        "generate_binary_strings",
        exercises.generate_binary_strings,
        (
            TestCase("length two", (2,), ["00", "01", "10", "11"]),
            TestCase("length zero", (0,), [""]),
            TestCase("length one", (1,), ["0", "1"]),
        ),
    ),
    ExerciseTests(
        "all_subsets",
        exercises.all_subsets,
        (
            TestCase("two values", ([1, 2],), [[], [2], [1], [1, 2]]),
            TestCase("empty input", ([],), [[]]),
            TestCase("single value", ([3],), [[], [3]]),
        ),
    ),
    ExerciseTests(
        "linked_list_length",
        exercises.linked_list_length,
        (
            TestCase("three nodes", (_linked_list([1, 2, 3]),), 3),
            TestCase("empty list", (None,), 0),
            TestCase("single node", (_linked_list([7]),), 1),
        ),
    ),
    ExerciseTests(
        "linked_list_values",
        exercises.linked_list_values,
        (
            TestCase("three nodes", (_linked_list([1, 2, 3]),), [1, 2, 3]),
            TestCase("empty list", (None,), []),
            TestCase("negative values", (_linked_list([-1, 0]),), [-1, 0]),
        ),
    ),
    ExerciseTests(
        "linked_list_contains",
        exercises.linked_list_contains,
        (
            TestCase("target present", (_linked_list([1, 2, 3]), 2), True),
            TestCase("target absent", (_linked_list([1, 2, 3]), 9), False),
            TestCase("empty list", (None, 1), False),
        ),
    ),
    ExerciseTests(
        "reverse_linked_list",
        exercises.reverse_linked_list,
        (
            TestCase(
                "three nodes",
                (_linked_list([1, 2, 3]),),
                _linked_list([3, 2, 1]),
                allows_mutation=True,
            ),
            TestCase(
                "single node",
                (_linked_list([5]),),
                _linked_list([5]),
                allows_mutation=True,
            ),
            TestCase("empty list", (None,), None, allows_mutation=True),
        ),
    ),
    ExerciseTests(
        "middle_linked_value",
        exercises.middle_linked_value,
        (
            TestCase("even length", (_linked_list([1, 2, 3, 4]),), 3),
            TestCase("odd length", (_linked_list([1, 2, 3, 4, 5]),), 3),
            TestCase("empty list", (None,), None),
            TestCase("single node", (_linked_list([8]),), 8),
        ),
    ),
    ExerciseTests(
        "tree_size",
        exercises.tree_size,
        (
            TestCase("four nodes", (_tree([1, 2, 3, None, 4]),), 4),
            TestCase("empty tree", (None,), 0),
            TestCase("single node", (_tree([7]),), 1),
        ),
    ),
    ExerciseTests(
        "tree_height",
        exercises.tree_height,
        (
            TestCase("three levels", (_tree([1, 2, 3, None, 4]),), 3),
            TestCase("empty tree", (None,), 0),
            TestCase("two levels", (_tree([1, 2, 3]),), 2),
        ),
    ),
    ExerciseTests(
        "tree_value_sum",
        exercises.tree_value_sum,
        (
            TestCase("mixed signs", (_tree([1, -2, 3]),), 2),
            TestCase("empty tree", (None,), 0),
            TestCase("several nodes", (_tree([5, 2, 4, 1]),), 12),
        ),
    ),
    ExerciseTests(
        "inorder_values",
        exercises.inorder_values,
        (
            TestCase("uneven tree", (_tree([1, 2, 3, None, 4]),), [2, 4, 1, 3]),
            TestCase("empty tree", (None,), []),
            TestCase("binary search tree", (_tree([2, 1, 3]),), [1, 2, 3]),
        ),
    ),
    ExerciseTests(
        "level_order_values",
        exercises.level_order_values,
        (
            TestCase("uneven tree", (_tree([1, 2, 3, None, 4]),), [1, 2, 3, 4]),
            TestCase("empty tree", (None,), []),
            TestCase("right branch", (_tree([1, None, 2, None, 3]),), [1, 2, 3]),
        ),
    ),
    ExerciseTests(
        "breadth_first_order",
        exercises.breadth_first_order,
        (
            TestCase(
                "branching graph",
                ({"A": ["B", "C"], "B": ["D"], "C": [], "D": []}, "A"),
                ["A", "B", "C", "D"],
            ),
            TestCase(
                "cycle visited once",
                ({"A": ["B"], "B": ["A"]}, "A"),
                ["A", "B"],
            ),
            TestCase("isolated node", ({"A": []}, "A"), ["A"]),
        ),
    ),
    ExerciseTests(
        "depth_first_order",
        exercises.depth_first_order,
        (
            TestCase(
                "branching graph",
                ({"A": ["B", "C"], "B": ["D"], "C": [], "D": []}, "A"),
                ["A", "B", "D", "C"],
            ),
            TestCase(
                "shared neighbor",
                ({"A": ["B", "C"], "B": ["C"], "C": []}, "A"),
                ["A", "B", "C"],
            ),
            TestCase("isolated node", ({"A": []}, "A"), ["A"]),
        ),
    ),
    ExerciseTests(
        "graph_has_path",
        exercises.graph_has_path,
        (
            TestCase(
                "reachable target",
                ({"A": ["B"], "B": ["C"], "C": []}, "A", "C"),
                True,
            ),
            TestCase(
                "unreachable target",
                ({"A": ["B"], "B": [], "C": []}, "A", "C"),
                False,
            ),
            TestCase("same node", ({"A": []}, "A", "A"), True),
        ),
    ),
    ExerciseTests(
        "connected_component_count",
        exercises.connected_component_count,
        (
            TestCase("edge and isolated node", ({0: [1], 1: [0], 2: []},), 2),
            TestCase("empty graph", ({},), 0),
            TestCase("one component", ({0: [1], 1: [0, 2], 2: [1]},), 1),
        ),
    ),
    ExerciseTests(
        "has_directed_cycle",
        exercises.has_directed_cycle,
        (
            TestCase("two-node cycle", ({"A": ["B"], "B": ["A"]},), True),
            TestCase(
                "directed acyclic graph",
                ({"A": ["B", "C"], "B": ["C"], "C": []},),
                False,
            ),
            TestCase("self loop", ({"A": ["A"]},), True),
            TestCase("empty graph", ({},), False),
        ),
    ),
    ExerciseTests(
        "climbing_ways",
        exercises.climbing_ways,
        (
            TestCase("zero steps", (0,), 1),
            TestCase("one step", (1,), 1),
            TestCase("four steps", (4,), 5),
        ),
    ),
    ExerciseTests(
        "maximum_non_adjacent_sum",
        exercises.maximum_non_adjacent_sum,
        (
            TestCase("alternating choices", ([2, 7, 9, 3, 1],), 12),
            TestCase("empty input", ([],), 0),
            TestCase("both ends", ([5, 1, 1, 5],), 10),
            TestCase("all zeroes", ([0, 0],), 0),
        ),
    ),
    ExerciseTests(
        "minimum_coin_count",
        exercises.minimum_coin_count,
        (
            TestCase("non-greedy optimum", ([1, 3, 4], 6), 2),
            TestCase("impossible amount", ([2], 3), -1),
            TestCase("zero amount", ([], 0), 0),
            TestCase("reused coin", ([2, 5], 10), 2),
        ),
    ),
    ExerciseTests(
        "grid_path_count",
        exercises.grid_path_count,
        (
            TestCase("square grid", (3, 3), 6),
            TestCase("single row", (1, 5), 1),
            TestCase("rectangular grid", (2, 3), 3),
        ),
    ),
)


class Judge:
    """Runs test cases while isolating their mutable inputs."""

    def __init__(self, exercise_tests: Sequence[ExerciseTests]) -> None:
        self._exercise_tests = tuple(exercise_tests)

    @property
    def exercise_names(self) -> tuple[str, ...]:
        return tuple(exercise.name for exercise in self._exercise_tests)

    def run(self, selected_names: set[str]) -> bool:
        selected = [
            exercise
            for exercise in self._exercise_tests
            if not selected_names or exercise.name in selected_names
        ]
        passed_function_count = 0
        failed_function_count = 0
        skipped_function_count = 0
        detailed_output = bool(selected_names)
        reported_exercise = False

        for exercise in selected:
            results = [
                (case, *self._run_case(exercise.function, case))
                for case in exercise.cases
            ]
            exercise_passed = self._count(results, CaseStatus.PASSED)
            exercise_failed = self._count(results, CaseStatus.FAILED)
            exercise_skipped = self._count(results, CaseStatus.SKIPPED)
            if exercise_failed:
                failed_function_count += 1
            elif exercise_skipped:
                skipped_function_count += 1
            else:
                passed_function_count += 1

            if detailed_output:
                if reported_exercise:
                    print()
                print(exercise.name)
                for case, status, detail in results:
                    suffix = f": {detail}" if detail else ""
                    print(f"  {status.colored_label}  {case.name}{suffix}")
                print(
                    "  Result: "
                    f"{self._format_count(CaseStatus.PASSED, exercise_passed)}, "
                    f"{self._format_count(CaseStatus.FAILED, exercise_failed)}, "
                    f"{self._format_count(CaseStatus.SKIPPED, exercise_skipped)}"
                )
                reported_exercise = True
            elif exercise_failed:
                print(f"{CaseStatus.FAILED.colored_label} {exercise.name}")
                for case, status, detail in results:
                    if status is CaseStatus.FAILED:
                        print(f"  {status.colored_label}  {case.name}: {detail}")
                reported_exercise = True
            elif not exercise_skipped:
                print(f"{CaseStatus.PASSED.colored_label} {exercise.name}")
                reported_exercise = True

        if reported_exercise:
            print()
        print(
            "Total functions: "
            f"{self._format_count(CaseStatus.PASSED, passed_function_count)}, "
            f"{self._format_count(CaseStatus.FAILED, failed_function_count)}, "
            f"{self._format_count(CaseStatus.SKIPPED, skipped_function_count)}"
        )
        return failed_function_count == 0

    @staticmethod
    def _count(
        results: Sequence[tuple[TestCase, CaseStatus, str]], status: CaseStatus
    ) -> int:
        return sum(result_status is status for _, result_status, _ in results)

    @staticmethod
    def _format_count(status: CaseStatus, count: int) -> str:
        return f"{status.colored_label} {count}"

    @staticmethod
    def _run_case(
        function: Callable[..., Any], case: TestCase
    ) -> tuple[CaseStatus, str]:
        arguments = deepcopy(case.arguments)
        original_arguments = deepcopy(arguments)

        try:
            actual = function(*arguments)
        except NotImplementedError as error:
            return CaseStatus.SKIPPED, str(error) or "not implemented"
        except Exception as error:  # The judge should report errors and continue.
            return CaseStatus.FAILED, f"raised {type(error).__name__}: {error}"

        if not case.allows_mutation and arguments != original_arguments:
            return CaseStatus.FAILED, "mutated its input arguments"
        if actual != case.expected:
            return CaseStatus.FAILED, f"expected {case.expected!r}, got {actual!r}"
        return CaseStatus.PASSED, ""


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("exercises", nargs="*", help="function names to run")
    parser.add_argument("--list", action="store_true", help="list available exercises")
    return parser.parse_args()


def main() -> int:
    arguments = parse_arguments()
    judge = Judge(EXERCISE_TESTS)

    if arguments.list:
        print("\n".join(judge.exercise_names))
        return 0

    requested_names = set(arguments.exercises)
    unknown_names = requested_names.difference(judge.exercise_names)
    if unknown_names:
        names = ", ".join(sorted(unknown_names))
        print(f"Unknown exercise name(s): {names}")
        print("Use --list to see the available names.")
        return 2

    return 0 if judge.run(requested_names) else 1


if __name__ == "__main__":
    raise SystemExit(main())
