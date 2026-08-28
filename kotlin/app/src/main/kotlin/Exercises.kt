/** Short Kotlin exercises for coding-interview preparation. */

// =============================================================================
// Topic 1: Collections and iteration
// =============================================================================

/** Return the squares of the even numbers, preserving their input order.
 *
 * Example: selectEvenSquares(listOf(1, 2, 4, 5)) == listOf(4, 16)
 */
fun selectEvenSquares(numbers: List<Int>): List<Int> {
    TODO("Implement selectEvenSquares")
}

/** Return (index, character) pairs for every character in [text].
 *
 * Spaces and punctuation count as characters.
 * Example: indexedCharacters("hi") == listOf(0 to 'h', 1 to 'i')
 */
fun indexedCharacters(text: String): List<Pair<Int, Char>> {
    TODO("Implement indexedCharacters")
}

/** Return the sum of each adjacent pair in [numbers].
 *
 * Inputs with fewer than two values return an empty list.
 * Example: adjacentSums(listOf(1, 4, -2)) == listOf(5, 2)
 */
fun adjacentSums(numbers: List<Int>): List<Int> {
    TODO("Implement adjacentSums")
}

/** Return a new list with [values] rotated left by [steps] positions.
 *
 * [steps] is non-negative and may exceed the list size. An empty input
 * returns an empty list. Do not mutate [values].
 */
fun rotateLeft(values: List<Int>, steps: Int): List<Int> {
    TODO("Implement rotateLeft")
}

/** Flatten one level of nested integer lists, preserving their order.
 *
 * Example: flattenOnce(listOf(listOf(1, 2), emptyList(), listOf(3)))
 * returns listOf(1, 2, 3).
 */
fun flattenOnce(groups: List<List<Int>>): List<Int> {
    TODO("Implement flattenOnce")
}

/** Split [values] into consecutive lists containing at most [size] items.
 *
 * [size] is always positive. The final chunk may be shorter. Do not mutate
 * [values].
 */
fun chunkValues(values: List<Int>, size: Int): List<List<Int>> {
    TODO("Implement chunkValues")
}

// =============================================================================
// Topic 2: Maps and sets
// =============================================================================

/** Return a map containing the occurrence count of each value. */
fun frequencyMap(values: List<String>): Map<String, Int> {
    TODO("Implement frequencyMap")
}

/** Return the first value that occurs once, or null if none exists. */
fun firstUniqueValue(values: List<Int>): Int? {
    TODO("Implement firstUniqueValue")
}

/** Map each distinct value to the indices where it occurs.
 *
 * Preserve the input order within every index list.
 */
fun groupIndices(values: List<String>): Map<String, List<Int>> {
    TODO("Implement groupIndices")
}

/** Return the distinct values present in both input lists. */
fun commonValues(left: List<Int>, right: List<Int>): Set<Int> {
    TODO("Implement commonValues")
}

/** Return indices of the first pair encountered whose values sum to [target].
 *
 * Scan from left to right and return the earlier matching index with the
 * current index. An input has at most one valid pair. Return null if no pair
 * exists.
 */
fun twoSumIndices(numbers: List<Int>, target: Int): Pair<Int, Int>? {
    TODO("Implement twoSumIndices")
}

// =============================================================================
// Topic 3: Strings
// =============================================================================

/** Return lowercase words split on any whitespace.
 *
 * Punctuation remains part of a word.
 */
fun normalizeWords(text: String): List<String> {
    TODO("Implement normalizeWords")
}

/** Return whether the letters and digits form a case-insensitive palindrome.
 *
 * Ignore all non-alphanumeric characters. An empty normalized string is a
 * palindrome.
 */
fun isNormalizedPalindrome(text: String): Boolean {
    TODO("Implement isNormalizedPalindrome")
}

/** Encode each run as its character followed by its count.
 *
 * The input contains only letters. Return an empty string for empty input.
 * Example: runLengthEncode("aaabbc") == "a3b2c1"
 */
fun runLengthEncode(text: String): String {
    TODO("Implement runLengthEncode")
}

/** Return the longest prefix shared by every word.
 *
 * Return an empty string when [words] is empty or has no common prefix.
 */
fun longestCommonPrefix(words: List<String>): String {
    TODO("Implement longestCommonPrefix")
}

/** Return whether two case-sensitive strings contain equal character counts.
 *
 * Spaces and punctuation count as characters.
 */
fun areAnagrams(left: String, right: String): Boolean {
    TODO("Implement areAnagrams")
}

// =============================================================================
// Topic 4: Sorting and binary search
// =============================================================================

/** Return words ordered by length, then alphabetically to break ties.
 *
 * Do not mutate [words].
 */
fun sortByLength(words: List<String>): List<String> {
    TODO("Implement sortByLength")
}

/** Return the [k] most frequent values in deterministic order.
 *
 * Order by decreasing frequency, then increasing numeric value. [k] is
 * between zero and the number of distinct values.
 */
fun topKFrequent(values: List<Int>, k: Int): List<Int> {
    TODO("Implement topKFrequent")
}

/** Return [target]'s index in a sorted list of distinct values, or -1. */
fun binarySearch(values: List<Int>, target: Int): Int {
    TODO("Implement binarySearch")
}

/** Return the index where [target] should be inserted to keep the list sorted.
 *
 * [values] may contain duplicates. Insert before existing equal values.
 */
fun lowerBound(values: List<Int>, target: Int): Int {
    TODO("Implement lowerBound")
}

/** Merge two sorted lists into a new sorted list containing all values.
 *
 * Preserve duplicates and do not mutate either input.
 */
fun mergeSorted(left: List<Int>, right: List<Int>): List<Int> {
    TODO("Implement mergeSorted")
}

// =============================================================================
// Topic 5: Stacks, queues, and priority queues
// =============================================================================

/** Return whether a string of ()[]{} brackets is correctly balanced. */
fun hasBalancedBrackets(text: String): Boolean {
    TODO("Implement hasBalancedBrackets")
}

/** Evaluate a valid postfix expression containing integers and +, -, *. */
fun evaluatePostfix(tokens: List<String>): Int {
    TODO("Implement evaluatePostfix")
}

/** Return the next greater value to the right of each number, or -1. */
fun nextGreaterValues(numbers: List<Int>): List<Int> {
    TODO("Implement nextGreaterValues")
}

/** Return up to the last [k] values in original order using a queue.
 *
 * [k] is positive.
 */
fun lastKItems(values: List<Int>, k: Int): List<Int> {
    TODO("Implement lastKItems")
}

/** Return the [k] largest values in descending order using a priority queue.
 *
 * Preserve duplicates. [k] is between zero and [values].size.
 */
fun kLargest(values: List<Int>, k: Int): List<Int> {
    TODO("Implement kLargest")
}

// =============================================================================
// Topic 6: Two pointers and sliding windows
// =============================================================================

/** Return whether a sorted list contains two values summing to [target].
 *
 * Use two different positions.
 */
fun hasPairWithSum(numbers: List<Int>, target: Int): Boolean {
    TODO("Implement hasPairWithSum")
}

/** Return the distinct values from a sorted list in ascending order.
 *
 * Do not mutate [numbers].
 */
fun deduplicateSorted(numbers: List<Int>): List<Int> {
    TODO("Implement deduplicateSorted")
}

/** Return a new list with zeroes after all nonzero values.
 *
 * Preserve the relative order of nonzero values and do not mutate [numbers].
 */
fun moveZeroesToEnd(numbers: List<Int>): List<Int> {
    TODO("Implement moveZeroesToEnd")
}

/** Return the largest sum among consecutive windows of length [size].
 *
 * [size] is between one and [numbers].size.
 */
fun maximumWindowSum(numbers: List<Int>, size: Int): Int {
    TODO("Implement maximumWindowSum")
}

/** Return the length of the longest substring without repeated characters. */
fun longestUniqueSubstringLength(text: String): Int {
    TODO("Implement longestUniqueSubstringLength")
}

// =============================================================================
// Topic 7: Prefix sums and intervals
// =============================================================================

/** Return prefix sums beginning with zero.
 *
 * Result index i contains the sum of numbers before i.
 */
fun buildPrefixSums(numbers: List<Int>): List<Int> {
    TODO("Implement buildPrefixSums")
}

/** Return the sum from [start] inclusive to [end] exclusive.
 *
 * [prefixSums] has the format returned by [buildPrefixSums], and
 * 0 <= start <= end < prefixSums.size.
 */
fun rangeSum(prefixSums: List<Int>, start: Int, end: Int): Int {
    TODO("Implement rangeSum")
}

/** Return the first index with equal sums on its left and right, or -1. */
fun pivotIndex(numbers: List<Int>): Int {
    TODO("Implement pivotIndex")
}

data class Interval(val start: Int, val end: Int) {
    init {
        require(start <= end) { "Interval start must not exceed its end" }
    }
}

/** Merge overlapping closed intervals and return them sorted by start.
 *
 * Touching endpoints count as overlap. Do not mutate [intervals].
 */
fun mergeIntervals(intervals: List<Interval>): List<Interval> {
    TODO("Implement mergeIntervals")
}

/** Return whether two closed intervals share at least one point. */
fun intervalsOverlap(first: Interval, second: Interval): Boolean {
    TODO("Implement intervalsOverlap")
}

// =============================================================================
// Topic 8: Recursion and backtracking
// =============================================================================

/** Return the factorial of a non-negative integer using recursion.
 *
 * Define 0! as 1.
 */
fun factorialRecursive(number: Int): Int {
    TODO("Implement factorialRecursive")
}

/** Return the sum of all values using recursion instead of sum().
 *
 * Return zero for an empty list. Do not mutate [numbers].
 */
fun recursiveSum(numbers: List<Int>): Int {
    TODO("Implement recursiveSum")
}

/** Return [text] reversed using recursion. */
fun reverseTextRecursive(text: String): String {
    TODO("Implement reverseTextRecursive")
}

/** Return every binary string of [length], exploring 0 before 1.
 *
 * [length] is non-negative. For zero, return a list containing the empty
 * string.
 */
fun generateBinaryStrings(length: Int): List<String> {
    TODO("Implement generateBinaryStrings")
}

/** Return every subset of distinct values using backtracking.
 *
 * At each position, explore excluding the value before including it.
 * Preserve input order inside a subset.
 */
fun allSubsets(values: List<Int>): List<List<Int>> {
    TODO("Implement allSubsets")
}

// =============================================================================
// Topic 9: Linked lists
// =============================================================================

data class ListNode(var value: Int, var next: ListNode? = null) {
    companion object {
        fun fromValues(values: List<Int>): ListNode? {
            var head: ListNode? = null
            for (value in values.asReversed()) {
                head = ListNode(value, head)
            }
            return head
        }
    }

    internal fun deepCopy(): ListNode = ListNode(value, next?.deepCopy())
}

/** Return the number of nodes reachable from [head]. */
fun linkedListLength(head: ListNode?): Int {
    TODO("Implement linkedListLength")
}

/** Return node values from head to tail without modifying the list. */
fun linkedListValues(head: ListNode?): List<Int> {
    TODO("Implement linkedListValues")
}

/** Return whether any node reachable from [head] contains [target]. */
fun linkedListContains(head: ListNode?, target: Int): Boolean {
    TODO("Implement linkedListContains")
}

/** Reverse the list in place and return its new head.
 *
 * Return null for an empty list.
 */
fun reverseLinkedList(head: ListNode?): ListNode? {
    TODO("Implement reverseLinkedList")
}

/** Return the middle node's value, or null for an empty list.
 *
 * For an even number of nodes, return the second middle value.
 */
fun middleLinkedValue(head: ListNode?): Int? {
    TODO("Implement middleLinkedValue")
}

// =============================================================================
// Topic 10: Trees
// =============================================================================

data class TreeNode(
    var value: Int,
    var left: TreeNode? = null,
    var right: TreeNode? = null,
) {
    companion object {
        fun fromLevelOrder(values: List<Int?>): TreeNode? {
            val rootValue = values.firstOrNull() ?: return null
            val root = TreeNode(rootValue)
            val parents = ArrayDeque<TreeNode>()
            parents.addLast(root)
            var childIndex = 1

            while (parents.isNotEmpty() && childIndex < values.size) {
                val parent = parents.removeFirst()
                values[childIndex++]?.let { value ->
                    parent.left = TreeNode(value)
                    parents.addLast(parent.left!!)
                }
                if (childIndex < values.size) {
                    values[childIndex++]?.let { value ->
                        parent.right = TreeNode(value)
                        parents.addLast(parent.right!!)
                    }
                }
            }
            return root
        }
    }

    internal fun deepCopy(): TreeNode =
        TreeNode(value, left?.deepCopy(), right?.deepCopy())
}

/** Return the number of nodes in the binary tree. An empty tree has size zero. */
fun treeSize(root: TreeNode?): Int {
    TODO("Implement treeSize")
}

/** Return the number of nodes on the longest root-to-leaf path.
 *
 * An empty tree has height zero and a leaf has height one.
 */
fun treeHeight(root: TreeNode?): Int {
    TODO("Implement treeHeight")
}

/** Return the sum of every node value. An empty tree has sum zero. */
fun treeValueSum(root: TreeNode?): Int {
    TODO("Implement treeValueSum")
}

/** Return values from an in-order traversal: left, root, then right. */
fun inorderValues(root: TreeNode?): List<Int> {
    TODO("Implement inorderValues")
}

/** Return values breadth-first, from the root level downward.
 *
 * Preserve left-to-right order within each level. An empty tree returns an
 * empty list.
 */
fun levelOrderValues(root: TreeNode?): List<Int> {
    TODO("Implement levelOrderValues")
}

// =============================================================================
// Topic 11: Graphs
// =============================================================================

/** Return the breadth-first traversal order from [start].
 *
 * Visit neighbors in their listed order and visit each node once. Every
 * referenced node is a key in the directed adjacency-list [graph].
 */
fun breadthFirstOrder(graph: Map<String, List<String>>, start: String): List<String> {
    TODO("Implement breadthFirstOrder")
}

/** Return the recursive depth-first traversal order from [start].
 *
 * Visit neighbors in their listed order and visit each node once.
 */
fun depthFirstOrder(graph: Map<String, List<String>>, start: String): List<String> {
    TODO("Implement depthFirstOrder")
}

/** Return whether [target] is reachable from [start] in a directed graph.
 *
 * A node is reachable from itself. The graph may contain cycles.
 */
fun graphHasPath(
    graph: Map<String, List<String>>,
    start: String,
    target: String,
): Boolean {
    TODO("Implement graphHasPath")
}

/** Return the number of connected components in an undirected graph.
 *
 * Every node, including isolated nodes, is a key in [graph].
 */
fun connectedComponentCount(graph: Map<Int, List<Int>>): Int {
    TODO("Implement connectedComponentCount")
}

/** Return whether a directed graph contains a cycle.
 *
 * Every referenced node is a key in [graph]. A self-loop is a cycle. Hint:
 * distinguish nodes currently being explored from completed nodes.
 */
fun hasDirectedCycle(graph: Map<String, List<String>>): Boolean {
    TODO("Implement hasDirectedCycle")
}

// =============================================================================
// Topic 12: Dynamic programming (allow 3-5 minutes each)
// =============================================================================

/** Return the number of ways to climb [steps] using moves of one or two.
 *
 * [steps] is non-negative. There is one way to climb zero steps. The state
 * for step i is the sum of the previous two states.
 */
fun climbingWays(steps: Int): Int {
    TODO("Implement climbingWays")
}

/** Return the largest sum obtainable without choosing adjacent values.
 *
 * All values are non-negative; choosing nothing yields zero. Track the best
 * totals including or excluding each position.
 */
fun maximumNonAdjacentSum(numbers: List<Int>): Int {
    TODO("Implement maximumNonAdjacentSum")
}

/** Return the fewest coins needed to form [amount], or -1 if impossible.
 *
 * Coin values are positive and reusable; [amount] is non-negative. Let each
 * state store the fewest coins needed for that intermediate amount.
 */
fun minimumCoinCount(coins: List<Int>, amount: Int): Int {
    TODO("Implement minimumCoinCount")
}

/** Return paths from the top-left to bottom-right of a rectangular grid.
 *
 * [rows] and [columns] are positive. Moves may go only right or down. Each
 * cell's state is the sum of the state above it and the state to its left.
 */
fun gridPathCount(rows: Int, columns: Int): Int {
    TODO("Implement gridPathCount")
}
