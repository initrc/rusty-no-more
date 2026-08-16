"""Short Python exercises for coding-interview preparation."""

from __future__ import annotations

from dataclasses import dataclass

# =============================================================================
# Topic 1: Sequences and iteration
# =============================================================================


def select_even_squares(numbers: list[int]) -> list[int]:
    """Return the squares of the even numbers, preserving their input order.

    Example: ``select_even_squares([1, 2, 4, 5]) == [4, 16]``
    """
    raise NotImplementedError("Implement select_even_squares")


def indexed_characters(text: str) -> list[tuple[int, str]]:
    """Return ``(index, character)`` pairs for every character in ``text``.

    Spaces and punctuation count as characters.
    Example: ``indexed_characters("hi") == [(0, "h"), (1, "i")]``
    """
    raise NotImplementedError("Implement indexed_characters")


def adjacent_sums(numbers: list[int]) -> list[int]:
    """Return the sum of each adjacent pair in ``numbers``.

    Inputs with fewer than two values return an empty list.
    Example: ``adjacent_sums([1, 4, -2]) == [5, 2]``
    """
    raise NotImplementedError("Implement adjacent_sums")


def rotate_left(values: list[int], steps: int) -> list[int]:
    """Return a new list with ``values`` rotated left by ``steps`` positions.

    ``steps`` is non-negative and may exceed the list length. An empty input
    returns an empty list. Do not mutate ``values``.
    Example: ``rotate_left([1, 2, 3, 4], 1) == [2, 3, 4, 1]``
    """
    raise NotImplementedError("Implement rotate_left")


def flatten_once(groups: list[list[int]]) -> list[int]:
    """Flatten one level of nested integer lists, preserving their order.

    Example: ``flatten_once([[1, 2], [], [3]]) == [1, 2, 3]``
    """
    raise NotImplementedError("Implement flatten_once")


def chunk_values(values: list[int], size: int) -> list[list[int]]:
    """Split ``values`` into consecutive lists containing at most ``size`` items.

    ``size`` is always positive. The final chunk may be shorter. Do not mutate
    ``values``.
    Example: ``chunk_values([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]``
    """
    raise NotImplementedError("Implement chunk_values")


# =============================================================================
# Topic 2: Dictionaries and sets
# =============================================================================


def frequency_map(values: list[str]) -> dict[str, int]:
    """Return a dictionary containing the occurrence count of each value.

    Example: ``frequency_map(["a", "b", "a"]) == {"a": 2, "b": 1}``
    """
    raise NotImplementedError("Implement frequency_map")


def first_unique_value(values: list[int]) -> int | None:
    """Return the first value that occurs once, or ``None`` if none exists.

    Example: ``first_unique_value([4, 2, 4, 3, 2]) == 3``
    """
    raise NotImplementedError("Implement first_unique_value")


def group_indices(values: list[str]) -> dict[str, list[int]]:
    """Map each distinct value to the indices where it occurs.

    Preserve the input order within every index list.
    Example: ``group_indices(["a", "b", "a"]) == {"a": [0, 2], "b": [1]}``
    """
    raise NotImplementedError("Implement group_indices")


def common_values(left: list[int], right: list[int]) -> set[int]:
    """Return the distinct values present in both input lists.

    Example: ``common_values([1, 2, 2], [2, 3]) == {2}``
    """
    raise NotImplementedError("Implement common_values")


def two_sum_indices(numbers: list[int], target: int) -> tuple[int, int] | None:
    """Return indices of the first pair encountered whose values sum to target.

    Scan from left to right and return the earlier matching index with the
    current index. An input has at most one valid pair. Return ``None`` if no
    pair exists. Example: ``two_sum_indices([2, 7, 11], 9) == (0, 1)``
    """
    raise NotImplementedError("Implement two_sum_indices")


# =============================================================================
# Topic 3: Strings
# =============================================================================


def normalize_words(text: str) -> list[str]:
    """Return lowercase words split on any whitespace.

    Punctuation remains part of a word.
    Example: ``normalize_words("  Hello  WORLD ") == ["hello", "world"]``
    """
    raise NotImplementedError("Implement normalize_words")


def is_normalized_palindrome(text: str) -> bool:
    """Return whether the letters and digits form a case-insensitive palindrome.

    Ignore all non-alphanumeric characters. An empty normalized string is a
    palindrome. Example: ``is_normalized_palindrome("A man, a plan, a canal: Panama!")``
    returns ``True``.
    """
    raise NotImplementedError("Implement is_normalized_palindrome")


def run_length_encode(text: str) -> str:
    """Encode each run as its character followed by its count.

    The input contains only letters. Return an empty string for empty input.
    Example: ``run_length_encode("aaabbc") == "a3b2c1"``
    """
    raise NotImplementedError("Implement run_length_encode")


def longest_common_prefix(words: list[str]) -> str:
    """Return the longest prefix shared by every word.

    Return an empty string when ``words`` is empty or has no common prefix.
    Example: ``longest_common_prefix(["flower", "flow", "flight"]) == "fl"``
    """
    raise NotImplementedError("Implement longest_common_prefix")


def are_anagrams(left: str, right: str) -> bool:
    """Return whether two case-sensitive strings contain equal character counts.

    Spaces and punctuation count as characters.
    Example: ``are_anagrams("listen", "silent") is True``
    """
    raise NotImplementedError("Implement are_anagrams")


# =============================================================================
# Topic 4: Sorting and binary search
# =============================================================================


def sort_by_length(words: list[str]) -> list[str]:
    """Return words ordered by length, then alphabetically to break ties.

    Do not mutate ``words``.
    Example: ``sort_by_length(["pear", "fig", "apple"]) == ["fig", "pear", "apple"]``
    """
    raise NotImplementedError("Implement sort_by_length")


def top_k_frequent(values: list[int], k: int) -> list[int]:
    """Return the ``k`` most frequent values in deterministic order.

    Order by decreasing frequency, then increasing numeric value. ``k`` is
    between zero and the number of distinct values.
    Example: ``top_k_frequent([1, 1, 2, 2, 3], 2) == [1, 2]``
    """
    raise NotImplementedError("Implement top_k_frequent")


def binary_search(values: list[int], target: int) -> int:
    """Return ``target``'s index in a sorted list of distinct values, or ``-1``.

    Example: ``binary_search([1, 4, 7, 9], 7) == 2``
    """
    raise NotImplementedError("Implement binary_search")


def lower_bound(values: list[int], target: int) -> int:
    """Return the index where ``target`` should be inserted to keep the list sorted.

    ``values`` is sorted and may contain duplicates. Insert before existing equal
    values. Example: ``lower_bound([1, 3, 3, 5], 3) == 1``
    """
    raise NotImplementedError("Implement lower_bound")


def merge_sorted(left: list[int], right: list[int]) -> list[int]:
    """Merge two sorted lists into a new sorted list containing all values.

    Preserve duplicates and do not mutate either input.
    Example: ``merge_sorted([1, 4], [2, 2, 5]) == [1, 2, 2, 4, 5]``
    """
    raise NotImplementedError("Implement merge_sorted")


# =============================================================================
# Topic 5: Stacks, queues, and heaps
# =============================================================================


def has_balanced_brackets(text: str) -> bool:
    """Return whether a string of ``()[]{}`` brackets is correctly balanced.

    Example: ``has_balanced_brackets("([]{})") is True``
    """
    raise NotImplementedError("Implement has_balanced_brackets")


def evaluate_postfix(tokens: list[str]) -> int:
    """Evaluate a valid postfix expression containing integers and ``+``, ``-``, ``*``.

    Example: ``evaluate_postfix(["2", "3", "+", "4", "*"]) == 20``
    """
    raise NotImplementedError("Implement evaluate_postfix")


def next_greater_values(numbers: list[int]) -> list[int]:
    """Return the next greater value to the right of each number, or ``-1``.

    Example: ``next_greater_values([2, 1, 3]) == [3, 3, -1]``
    """
    raise NotImplementedError("Implement next_greater_values")


def last_k_items(values: list[int], k: int) -> list[int]:
    """Return up to the last ``k`` values in their original order using a queue.

    ``k`` is positive. Example: ``last_k_items([1, 2, 3, 4], 2) == [3, 4]``
    """
    raise NotImplementedError("Implement last_k_items")


def k_largest(values: list[int], k: int) -> list[int]:
    """Return the ``k`` largest values in descending order using a heap.

    Preserve duplicates. ``k`` is between zero and ``len(values)``.
    Example: ``k_largest([3, 1, 4, 4], 2) == [4, 4]``
    """
    raise NotImplementedError("Implement k_largest")


# =============================================================================
# Topic 6: Two pointers and sliding windows
# =============================================================================


def has_pair_with_sum(numbers: list[int], target: int) -> bool:
    """Return whether a sorted list contains two values summing to ``target``.

    Use two different positions. Example: ``has_pair_with_sum([1, 2, 4, 7], 9)``
    returns ``True``.
    """
    raise NotImplementedError("Implement has_pair_with_sum")


def deduplicate_sorted(numbers: list[int]) -> list[int]:
    """Return the distinct values from a sorted list in ascending order.

    Do not mutate ``numbers``.
    Example: ``deduplicate_sorted([1, 1, 2, 2, 3]) == [1, 2, 3]``
    """
    raise NotImplementedError("Implement deduplicate_sorted")


def move_zeroes_to_end(numbers: list[int]) -> list[int]:
    """Return a new list with zeroes after all nonzero values.

    Preserve the relative order of nonzero values and do not mutate ``numbers``.
    Example: ``move_zeroes_to_end([0, 1, 0, 3]) == [1, 3, 0, 0]``
    """
    raise NotImplementedError("Implement move_zeroes_to_end")


def maximum_window_sum(numbers: list[int], size: int) -> int:
    """Return the largest sum among consecutive windows of length ``size``.

    ``size`` is between one and ``len(numbers)``.
    Example: ``maximum_window_sum([1, 4, 2, 10], 2) == 12``
    """
    raise NotImplementedError("Implement maximum_window_sum")


def longest_unique_substring_length(text: str) -> int:
    """Return the length of the longest substring without repeated characters.

    Example: ``longest_unique_substring_length("abcabcbb") == 3``
    """
    raise NotImplementedError("Implement longest_unique_substring_length")


# =============================================================================
# Topic 7: Prefix sums and intervals
# =============================================================================


def build_prefix_sums(numbers: list[int]) -> list[int]:
    """Return prefix sums beginning with zero.

    Result index ``i`` contains the sum of ``numbers[:i]``.
    Example: ``build_prefix_sums([2, -1, 3]) == [0, 2, 1, 4]``
    """
    raise NotImplementedError("Implement build_prefix_sums")


def range_sum(prefix_sums: list[int], start: int, end: int) -> int:
    """Return the sum from ``start`` inclusive to ``end`` exclusive.

    ``prefix_sums`` has the format returned by ``build_prefix_sums`` and
    ``0 <= start <= end < len(prefix_sums)``.
    Example: ``range_sum([0, 2, 1, 4], 1, 3) == 2``
    """
    raise NotImplementedError("Implement range_sum")


def pivot_index(numbers: list[int]) -> int:
    """Return the first index with equal sums on its left and right, or ``-1``.

    Example: ``pivot_index([1, 7, 3, 6, 5, 6]) == 3``
    """
    raise NotImplementedError("Implement pivot_index")


def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Merge overlapping closed intervals and return them sorted by start.

    Touching endpoints count as overlap. Do not mutate ``intervals``.
    Example: ``merge_intervals([(1, 3), (2, 4), (7, 8)]) == [(1, 4), (7, 8)]``
    """
    raise NotImplementedError("Implement merge_intervals")


def intervals_overlap(first: tuple[int, int], second: tuple[int, int]) -> bool:
    """Return whether two closed intervals share at least one point.

    Each interval's start is at most its end.
    Example: ``intervals_overlap((1, 3), (3, 5)) is True``
    """
    raise NotImplementedError("Implement intervals_overlap")


# =============================================================================
# Topic 8: Recursion and backtracking
# =============================================================================


def factorial_recursive(number: int) -> int:
    """Return the factorial of a non-negative integer using recursion.

    Define ``0!`` as ``1``. Example: ``factorial_recursive(5) == 120``
    """
    raise NotImplementedError("Implement factorial_recursive")


def recursive_sum(numbers: list[int]) -> int:
    """Return the sum of all values using recursion instead of ``sum``.

    Return zero for an empty list. Do not mutate ``numbers``.
    Example: ``recursive_sum([2, -1, 4]) == 5``
    """
    raise NotImplementedError("Implement recursive_sum")


def reverse_text_recursive(text: str) -> str:
    """Return ``text`` reversed using recursion.

    Example: ``reverse_text_recursive("code") == "edoc"``
    """
    raise NotImplementedError("Implement reverse_text_recursive")


def generate_binary_strings(length: int) -> list[str]:
    """Return every binary string of ``length``, exploring ``0`` before ``1``.

    ``length`` is non-negative. For zero, return a list containing the empty
    string. Example: ``generate_binary_strings(2) == ["00", "01", "10", "11"]``
    """
    raise NotImplementedError("Implement generate_binary_strings")


def all_subsets(values: list[int]) -> list[list[int]]:
    """Return every subset of distinct values using backtracking.

    At each position, explore excluding the value before including it. Preserve
    input order inside a subset. Example: ``all_subsets([1, 2])`` returns
    ``[[], [2], [1], [1, 2]]``.
    """
    raise NotImplementedError("Implement all_subsets")


# =============================================================================
# Topic 9: Linked lists
# =============================================================================


@dataclass
class ListNode:
    """A singly linked list node used by the linked-list exercises."""

    value: int
    next: ListNode | None = None

    @classmethod
    def from_values(cls, values: list[int]) -> ListNode | None:
        head = None
        for value in reversed(values):
            head = cls(value, head)
        return head


def linked_list_length(head: ListNode | None) -> int:
    """Return the number of nodes reachable from ``head``.

    Example: a list containing ``1 -> 2 -> 3`` has length ``3``.
    """
    raise NotImplementedError("Implement linked_list_length")


def linked_list_values(head: ListNode | None) -> list[int]:
    """Return node values from head to tail without modifying the list.

    Example: a list ``1 -> 2 -> 3`` returns ``[1, 2, 3]``.
    """
    raise NotImplementedError("Implement linked_list_values")


def linked_list_contains(head: ListNode | None, target: int) -> bool:
    """Return whether any node reachable from ``head`` contains ``target``.

    Example: ``linked_list_contains(1 -> 2 -> 3, 2)`` returns ``True``.
    """
    raise NotImplementedError("Implement linked_list_contains")


def reverse_linked_list(head: ListNode | None) -> ListNode | None:
    """Reverse the list in place and return its new head.

    Return ``None`` for an empty list. Example: ``1 -> 2 -> 3`` becomes
    ``3 -> 2 -> 1``.
    """
    raise NotImplementedError("Implement reverse_linked_list")


def middle_linked_value(head: ListNode | None) -> int | None:
    """Return the middle node's value, or ``None`` for an empty list.

    For an even number of nodes, return the second middle value.
    Example: ``middle_linked_value(1 -> 2 -> 3 -> 4) == 3``.
    """
    raise NotImplementedError("Implement middle_linked_value")


# =============================================================================
# Topic 10: Trees
# =============================================================================


@dataclass
class TreeNode:
    """A binary tree node used by the tree exercises."""

    value: int
    left: TreeNode | None = None
    right: TreeNode | None = None

    @classmethod
    def from_level_order(
        cls, values: list[int | None]
    ) -> TreeNode | None:
        if not values or values[0] is None:
            return None
        root = cls(values[0])
        parents = [root]
        child_index = 1
        for parent in parents:
            if child_index >= len(values):
                break
            child_value = values[child_index]
            if child_value is not None:
                parent.left = cls(child_value)
                parents.append(parent.left)
            child_index += 1
            if child_index < len(values):
                child_value = values[child_index]
                if child_value is not None:
                    parent.right = cls(child_value)
                    parents.append(parent.right)
            child_index += 1
        return root


def tree_size(root: TreeNode | None) -> int:
    """Return the number of nodes in the binary tree.

    An empty tree has size zero.
    """
    raise NotImplementedError("Implement tree_size")


def tree_height(root: TreeNode | None) -> int:
    """Return the number of nodes on the longest root-to-leaf path.

    An empty tree has height zero and a leaf has height one.
    """
    raise NotImplementedError("Implement tree_height")


def tree_value_sum(root: TreeNode | None) -> int:
    """Return the sum of every node value in the binary tree.

    An empty tree has sum zero.
    """
    raise NotImplementedError("Implement tree_value_sum")


def inorder_values(root: TreeNode | None) -> list[int]:
    """Return values from an in-order traversal: left, root, then right.

    Example: a root ``2`` with children ``1`` and ``3`` returns ``[1, 2, 3]``.
    """
    raise NotImplementedError("Implement inorder_values")


def level_order_values(root: TreeNode | None) -> list[int]:
    """Return values breadth-first, from the root level downward.

    Preserve left-to-right order within each level. An empty tree returns ``[]``.
    """
    raise NotImplementedError("Implement level_order_values")


# =============================================================================
# Topic 11: Graphs
# =============================================================================


def breadth_first_order(graph: dict[str, list[str]], start: str) -> list[str]:
    """Return the breadth-first traversal order from ``start``.

    Visit neighbors in their listed order and visit each node once. Every
    referenced node is a key in the directed adjacency-list ``graph``.
    """
    raise NotImplementedError("Implement breadth_first_order")


def depth_first_order(graph: dict[str, list[str]], start: str) -> list[str]:
    """Return the recursive depth-first traversal order from ``start``.

    Visit neighbors in their listed order and visit each node once. Every
    referenced node is a key in the directed adjacency-list ``graph``.
    """
    raise NotImplementedError("Implement depth_first_order")


def graph_has_path(
    graph: dict[str, list[str]], start: str, target: str
) -> bool:
    """Return whether ``target`` is reachable from ``start`` in a directed graph.

    A node is reachable from itself. The graph may contain cycles.
    """
    raise NotImplementedError("Implement graph_has_path")


def connected_component_count(graph: dict[int, list[int]]) -> int:
    """Return the number of connected components in an undirected graph.

    Every node, including isolated nodes, is a key in ``graph``.
    """
    raise NotImplementedError("Implement connected_component_count")


def has_directed_cycle(graph: dict[str, list[str]]) -> bool:
    """Return whether a directed graph contains a cycle.

    Every referenced node is a key in ``graph``. A self-loop is a cycle.
    Hint: distinguish nodes currently being explored from completed nodes.
    """
    raise NotImplementedError("Implement has_directed_cycle")


# =============================================================================
# Topic 12: Dynamic programming (allow 3-5 minutes each)
# =============================================================================


def climbing_ways(steps: int) -> int:
    """Return the number of ways to climb ``steps`` using moves of one or two.

    ``steps`` is non-negative. There is one way to climb zero steps. The state
    for step ``i`` is the sum of the previous two states.
    """
    raise NotImplementedError("Implement climbing_ways")


def maximum_non_adjacent_sum(numbers: list[int]) -> int:
    """Return the largest sum obtainable without choosing adjacent values.

    All values are non-negative; choosing nothing yields zero. Track the best
    totals including or excluding each position.
    Example: ``maximum_non_adjacent_sum([2, 7, 9, 3, 1]) == 12``
    """
    raise NotImplementedError("Implement maximum_non_adjacent_sum")


def minimum_coin_count(coins: list[int], amount: int) -> int:
    """Return the fewest coins needed to form ``amount``, or ``-1`` if impossible.

    Coin values are positive and reusable; ``amount`` is non-negative. Let each
    state store the fewest coins needed for that intermediate amount.
    Example: ``minimum_coin_count([1, 3, 4], 6) == 2``
    """
    raise NotImplementedError("Implement minimum_coin_count")


def grid_path_count(rows: int, columns: int) -> int:
    """Return paths from the top-left to bottom-right of a rectangular grid.

    ``rows`` and ``columns`` are positive. Moves may go only right or down. Each
    cell's state is the sum of the state above it and the state to its left.
    Example: ``grid_path_count(3, 3) == 6``
    """
    raise NotImplementedError("Implement grid_path_count")
