/** Command-line judge for the Kotlin interview exercises. */

private data class TestCase(
    val name: String,
    val arguments: List<Any?>,
    val expected: Any?,
    val allowsMutation: Boolean = false,
)

private data class ExerciseTests(
    val name: String,
    val function: Function<*>,
    val cases: List<TestCase>,
)

private enum class CaseStatus(val label: String, private val color: String) {
    PASSED("PASS", "\u001B[32m"),
    FAILED("FAIL", "\u001B[31m"),
    SKIPPED("SKIP", "\u001B[33m");

    val coloredLabel: String
        get() = "$color$label\u001B[0m"
}

private data class CaseResult(
    val case: TestCase,
    val status: CaseStatus,
    val detail: String = "",
)

private fun case(name: String, expected: Any?, vararg arguments: Any?): TestCase =
    TestCase(name, arguments.toList(), expected)

private fun mutatingCase(name: String, expected: Any?, vararg arguments: Any?): TestCase =
    TestCase(name, arguments.toList(), expected, allowsMutation = true)

private fun linkedList(vararg values: Int): ListNode? = ListNode.fromValues(values.toList())

private fun tree(vararg values: Int?): TreeNode? = TreeNode.fromLevelOrder(values.toList())

private fun exercise(
    name: String,
    function: Function<*>,
    vararg cases: TestCase,
): ExerciseTests = ExerciseTests(name, function, cases.toList())

private val exerciseTests = listOf(
    exercise(
        "selectEvenSquares",
        ::selectEvenSquares,
        case("mixed values", listOf(4, 16), listOf(1, 2, 4, 5)),
        case("empty input", emptyList<Int>(), emptyList<Int>()),
        case("negative values and zero", listOf(4, 0, 36), listOf(-2, -1, 0, 6)),
    ),
    exercise(
        "indexedCharacters",
        ::indexedCharacters,
        case("short word", listOf(0 to 'c', 1 to 'a', 2 to 't'), "cat"),
        case("empty text", emptyList<Pair<Int, Char>>(), ""),
        case("space is retained", listOf(0 to 'a', 1 to ' ', 2 to 'a'), "a a"),
    ),
    exercise(
        "adjacentSums",
        ::adjacentSums,
        case("three values", listOf(5, 2), listOf(1, 4, -2)),
        case("single value", emptyList<Int>(), listOf(7)),
        case("negative pair", listOf(-8), listOf(-3, -5)),
    ),
    exercise(
        "rotateLeft",
        ::rotateLeft,
        case("single step", listOf(2, 3, 4, 1), listOf(1, 2, 3, 4), 1),
        case("steps exceed size", listOf(3, 4, 1, 2), listOf(1, 2, 3, 4), 6),
        case("empty input", emptyList<Int>(), emptyList<Int>(), 99),
        case("zero steps", listOf(1, 2), listOf(1, 2), 0),
    ),
    exercise(
        "flattenOnce",
        ::flattenOnce,
        case("empty group included", listOf(1, 2, 3), listOf(listOf(1, 2), emptyList(), listOf(3))),
        case("no groups", emptyList<Int>(), emptyList<List<Int>>()),
        case("only empty groups", emptyList<Int>(), listOf(emptyList<Int>(), emptyList())),
    ),
    exercise(
        "chunkValues",
        ::chunkValues,
        case("partial final chunk", listOf(listOf(1, 2), listOf(3, 4), listOf(5)), listOf(1, 2, 3, 4, 5), 2),
        case("empty input", emptyList<List<Int>>(), emptyList<Int>(), 3),
        case("chunk larger than input", listOf(listOf(1, 2)), listOf(1, 2), 5),
        case("unit chunks", listOf(listOf(3), listOf(4)), listOf(3, 4), 1),
    ),
    exercise(
        "frequencyMap",
        ::frequencyMap,
        case("repeated values", mapOf("a" to 2, "b" to 1), listOf("a", "b", "a")),
        case("empty input", emptyMap<String, Int>(), emptyList<String>()),
        case("one distinct value", mapOf("x" to 3), listOf("x", "x", "x")),
    ),
    exercise(
        "firstUniqueValue",
        ::firstUniqueValue,
        case("unique value after repeats", 3, listOf(4, 2, 4, 3, 2)),
        case("no unique value", null, listOf(1, 1, 2, 2)),
        case("single value", 9, listOf(9)),
    ),
    exercise(
        "groupIndices",
        ::groupIndices,
        case("repeated values", mapOf("a" to listOf(0, 2), "b" to listOf(1)), listOf("a", "b", "a")),
        case("empty input", emptyMap<String, List<Int>>(), emptyList<String>()),
        case("one group", mapOf("x" to listOf(0, 1)), listOf("x", "x")),
    ),
    exercise(
        "commonValues",
        ::commonValues,
        case("duplicates collapse", setOf(2), listOf(1, 2, 2), listOf(2, 3)),
        case("disjoint inputs", emptySet<Int>(), listOf(1), listOf(2)),
        case("negative values", setOf(-1, 2), listOf(-1, 0, 2), listOf(2, -1)),
    ),
    exercise(
        "twoSumIndices",
        ::twoSumIndices,
        case("pair at beginning", 0 to 1, listOf(2, 7, 11), 9),
        case("pair later in input", 1 to 2, listOf(3, 2, 4), 6),
        case("no pair", null, listOf(1, 2, 3), 99),
    ),
    exercise(
        "normalizeWords",
        ::normalizeWords,
        case("mixed case and spaces", listOf("hello", "world"), "  Hello  WORLD "),
        case("all whitespace", emptyList<String>(), " \t\n"),
        case("punctuation retained", listOf("hi,", "there!"), "Hi, THERE!"),
    ),
    exercise(
        "isNormalizedPalindrome",
        ::isNormalizedPalindrome,
        case("phrase palindrome", true, "A man, a plan, a canal: Panama!"),
        case("not a palindrome", false, "race a car"),
        case("no alphanumeric characters", true, "! ?"),
    ),
    exercise(
        "runLengthEncode",
        ::runLengthEncode,
        case("several runs", "a3b2c1", "aaabbc"),
        case("empty text", "", ""),
        case("single character", "z1", "z"),
    ),
    exercise(
        "longestCommonPrefix",
        ::longestCommonPrefix,
        case("shared prefix", "fl", listOf("flower", "flow", "flight")),
        case("no words", "", emptyList<String>()),
        case("no shared prefix", "", listOf("dog", "racecar", "car")),
        case("single word", "solo", listOf("solo")),
    ),
    exercise(
        "areAnagrams",
        ::areAnagrams,
        case("same counts", true, "listen", "silent"),
        case("different counts", false, "rat", "car"),
        case("spaces count", true, "a b", "ab "),
        case("case sensitive", false, "A", "a"),
    ),
    exercise(
        "sortByLength",
        ::sortByLength,
        case("different lengths", listOf("fig", "pear", "apple"), listOf("pear", "fig", "apple")),
        case("alphabetical tie", listOf("ant", "cat", "dog"), listOf("dog", "ant", "cat")),
        case("empty input", emptyList<String>(), emptyList<String>()),
    ),
    exercise(
        "topKFrequent",
        ::topKFrequent,
        case("frequency order", listOf(1, 2), listOf(1, 1, 2, 2, 3), 2),
        case("numeric tie break", listOf(1, 2), listOf(3, 1, 2), 2),
        case("zero requested", emptyList<Int>(), listOf(1, 1), 0),
    ),
    exercise(
        "binarySearch",
        ::binarySearch,
        case("target present", 2, listOf(1, 4, 7, 9), 7),
        case("target absent", -1, listOf(1, 4, 7, 9), 5),
        case("empty input", -1, emptyList<Int>(), 3),
        case("first value", 0, listOf(2, 5), 2),
    ),
    exercise(
        "lowerBound",
        ::lowerBound,
        case("duplicate target", 1, listOf(1, 3, 3, 5), 3),
        case("insert at end", 3, listOf(1, 3, 5), 7),
        case("insert at beginning", 0, listOf(2, 4), 1),
        case("empty input", 0, emptyList<Int>(), 8),
    ),
    exercise(
        "mergeSorted",
        ::mergeSorted,
        case("interleaved values", listOf(1, 2, 2, 4, 5), listOf(1, 4), listOf(2, 2, 5)),
        case("one empty input", listOf(1, 3), emptyList<Int>(), listOf(1, 3)),
        case("duplicates from both", listOf(1, 1, 2, 2), listOf(1, 2), listOf(1, 2)),
    ),
    exercise(
        "hasBalancedBrackets",
        ::hasBalancedBrackets,
        case("nested brackets", true, "([]{})"),
        case("crossed brackets", false, "([)]"),
        case("missing closer", false, "(()"),
        case("empty text", true, ""),
    ),
    exercise(
        "evaluatePostfix",
        ::evaluatePostfix,
        case("multiple operations", 20, listOf("2", "3", "+", "4", "*")),
        case("operand order", 3, listOf("5", "2", "-")),
        case("negative integer", -6, listOf("-3", "2", "*")),
    ),
    exercise(
        "nextGreaterValues",
        ::nextGreaterValues,
        case("mixed values", listOf(3, 3, -1), listOf(2, 1, 3)),
        case("descending values", listOf(-1, -1, -1), listOf(3, 2, 1)),
        case("equal values", listOf(3, 3, -1), listOf(2, 2, 3)),
        case("empty input", emptyList<Int>(), emptyList<Int>()),
    ),
    exercise(
        "lastKItems",
        ::lastKItems,
        case("discard older values", listOf(3, 4), listOf(1, 2, 3, 4), 2),
        case("empty input", emptyList<Int>(), emptyList<Int>(), 3),
        case("limit exceeds size", listOf(1, 2), listOf(1, 2), 5),
    ),
    exercise(
        "kLargest",
        ::kLargest,
        case("duplicates retained", listOf(4, 4), listOf(3, 1, 4, 4), 2),
        case("zero requested", emptyList<Int>(), listOf(1, 2), 0),
        case("negative values", listOf(-1, -3), listOf(-4, -1, -3), 2),
    ),
    exercise(
        "hasPairWithSum",
        ::hasPairWithSum,
        case("pair exists", true, listOf(1, 2, 4, 7), 9),
        case("pair absent", false, listOf(1, 2, 4, 7), 20),
        case("equal values at different positions", true, listOf(3, 3), 6),
        case("one value cannot pair with itself", false, listOf(3), 6),
    ),
    exercise(
        "deduplicateSorted",
        ::deduplicateSorted,
        case("several duplicates", listOf(1, 2, 3), listOf(1, 1, 2, 2, 3)),
        case("empty input", emptyList<Int>(), emptyList<Int>()),
        case("already distinct", listOf(-1, 0, 2), listOf(-1, 0, 2)),
    ),
    exercise(
        "moveZeroesToEnd",
        ::moveZeroesToEnd,
        case("interspersed zeroes", listOf(1, 3, 0, 0), listOf(0, 1, 0, 3)),
        case("no zeroes", listOf(1, 2), listOf(1, 2)),
        case("only zeroes", listOf(0, 0), listOf(0, 0)),
    ),
    exercise(
        "maximumWindowSum",
        ::maximumWindowSum,
        case("best final window", 12, listOf(1, 4, 2, 10), 2),
        case("negative values", -3, listOf(-2, -1, -3), 2),
        case("window is full input", 3, listOf(1, 2), 2),
    ),
    exercise(
        "longestUniqueSubstringLength",
        ::longestUniqueSubstringLength,
        case("repeated sequence", 3, "abcabcbb"),
        case("empty text", 0, ""),
        case("one repeated character", 1, "bbbbb"),
        case("overlapping window", 3, "pwwkew"),
    ),
    exercise(
        "buildPrefixSums",
        ::buildPrefixSums,
        case("mixed signs", listOf(0, 2, 1, 4), listOf(2, -1, 3)),
        case("empty input", listOf(0), emptyList<Int>()),
        case("negative total", listOf(0, -2, -5), listOf(-2, -3)),
    ),
    exercise(
        "rangeSum",
        ::rangeSum,
        case("middle range", 2, listOf(0, 2, 1, 4), 1, 3),
        case("entire range", 4, listOf(0, 2, 1, 4), 0, 3),
        case("empty range", 0, listOf(0, 2, 1, 4), 2, 2),
    ),
    exercise(
        "pivotIndex",
        ::pivotIndex,
        case("middle pivot", 3, listOf(1, 7, 3, 6, 5, 6)),
        case("no pivot", -1, listOf(1, 2, 3)),
        case("single value", 0, listOf(0)),
        case("first index pivot", 0, listOf(2, 1, -1)),
    ),
    exercise(
        "mergeIntervals",
        ::mergeIntervals,
        case(
            "overlapping intervals",
            listOf(Interval(1, 4), Interval(7, 8)),
            listOf(Interval(1, 3), Interval(2, 4), Interval(7, 8)),
        ),
        case(
            "unsorted disjoint intervals",
            listOf(Interval(1, 2), Interval(5, 6)),
            listOf(Interval(5, 6), Interval(1, 2)),
        ),
        case("touching endpoints", listOf(Interval(1, 5)), listOf(Interval(1, 3), Interval(3, 5))),
        case("empty input", emptyList<Interval>(), emptyList<Interval>()),
    ),
    exercise(
        "intervalsOverlap",
        ::intervalsOverlap,
        case("touching endpoints", true, Interval(1, 3), Interval(3, 5)),
        case("separate intervals", false, Interval(1, 2), Interval(3, 4)),
        case("contained interval", true, Interval(1, 8), Interval(3, 4)),
    ),
    exercise(
        "factorialRecursive",
        ::factorialRecursive,
        case("zero", 1, 0),
        case("one", 1, 1),
        case("positive value", 120, 5),
    ),
    exercise(
        "recursiveSum",
        ::recursiveSum,
        case("mixed signs", 5, listOf(2, -1, 4)),
        case("empty input", 0, emptyList<Int>()),
        case("single value", 7, listOf(7)),
    ),
    exercise(
        "reverseTextRecursive",
        ::reverseTextRecursive,
        case("word", "edoc", "code"),
        case("empty text", "", ""),
        case("palindrome", "level", "level"),
    ),
    exercise(
        "generateBinaryStrings",
        ::generateBinaryStrings,
        case("length two", listOf("00", "01", "10", "11"), 2),
        case("length zero", listOf(""), 0),
        case("length one", listOf("0", "1"), 1),
    ),
    exercise(
        "allSubsets",
        ::allSubsets,
        case("two values", listOf(emptyList(), listOf(2), listOf(1), listOf(1, 2)), listOf(1, 2)),
        case("empty input", listOf(emptyList<Int>()), emptyList<Int>()),
        case("single value", listOf(emptyList(), listOf(3)), listOf(3)),
    ),
    exercise(
        "linkedListLength",
        ::linkedListLength,
        case("three nodes", 3, linkedList(1, 2, 3)),
        case("empty list", 0, null),
        case("single node", 1, linkedList(7)),
    ),
    exercise(
        "linkedListValues",
        ::linkedListValues,
        case("three nodes", listOf(1, 2, 3), linkedList(1, 2, 3)),
        case("empty list", emptyList<Int>(), null),
        case("negative values", listOf(-1, 0), linkedList(-1, 0)),
    ),
    exercise(
        "linkedListContains",
        ::linkedListContains,
        case("target present", true, linkedList(1, 2, 3), 2),
        case("target absent", false, linkedList(1, 2, 3), 9),
        case("empty list", false, null, 1),
    ),
    exercise(
        "reverseLinkedList",
        ::reverseLinkedList,
        mutatingCase("three nodes", linkedList(3, 2, 1), linkedList(1, 2, 3)),
        mutatingCase("single node", linkedList(5), linkedList(5)),
        mutatingCase("empty list", null, null),
    ),
    exercise(
        "middleLinkedValue",
        ::middleLinkedValue,
        case("even length", 3, linkedList(1, 2, 3, 4)),
        case("odd length", 3, linkedList(1, 2, 3, 4, 5)),
        case("empty list", null, null),
        case("single node", 8, linkedList(8)),
    ),
    exercise(
        "treeSize",
        ::treeSize,
        case("four nodes", 4, tree(1, 2, 3, null, 4)),
        case("empty tree", 0, null),
        case("single node", 1, tree(7)),
    ),
    exercise(
        "treeHeight",
        ::treeHeight,
        case("three levels", 3, tree(1, 2, 3, null, 4)),
        case("empty tree", 0, null),
        case("two levels", 2, tree(1, 2, 3)),
    ),
    exercise(
        "treeValueSum",
        ::treeValueSum,
        case("mixed signs", 2, tree(1, -2, 3)),
        case("empty tree", 0, null),
        case("several nodes", 12, tree(5, 2, 4, 1)),
    ),
    exercise(
        "inorderValues",
        ::inorderValues,
        case("uneven tree", listOf(2, 4, 1, 3), tree(1, 2, 3, null, 4)),
        case("empty tree", emptyList<Int>(), null),
        case("binary search tree", listOf(1, 2, 3), tree(2, 1, 3)),
    ),
    exercise(
        "levelOrderValues",
        ::levelOrderValues,
        case("uneven tree", listOf(1, 2, 3, 4), tree(1, 2, 3, null, 4)),
        case("empty tree", emptyList<Int>(), null),
        case("right branch", listOf(1, 2, 3), tree(1, null, 2, null, 3)),
    ),
    exercise(
        "breadthFirstOrder",
        ::breadthFirstOrder,
        case(
            "branching graph",
            listOf("A", "B", "C", "D"),
            mapOf(
                "A" to listOf("B", "C"),
                "B" to listOf("D"),
                "C" to emptyList(),
                "D" to emptyList(),
            ),
            "A",
        ),
        case("cycle visited once", listOf("A", "B"), mapOf("A" to listOf("B"), "B" to listOf("A")), "A"),
        case("isolated node", listOf("A"), mapOf("A" to emptyList<String>()), "A"),
    ),
    exercise(
        "depthFirstOrder",
        ::depthFirstOrder,
        case(
            "branching graph",
            listOf("A", "B", "D", "C"),
            mapOf(
                "A" to listOf("B", "C"),
                "B" to listOf("D"),
                "C" to emptyList(),
                "D" to emptyList(),
            ),
            "A",
        ),
        case(
            "shared neighbor",
            listOf("A", "B", "C"),
            mapOf("A" to listOf("B", "C"), "B" to listOf("C"), "C" to emptyList()),
            "A",
        ),
        case("isolated node", listOf("A"), mapOf("A" to emptyList<String>()), "A"),
    ),
    exercise(
        "graphHasPath",
        ::graphHasPath,
        case("reachable target", true, mapOf("A" to listOf("B"), "B" to listOf("C"), "C" to emptyList()), "A", "C"),
        case("unreachable target", false, mapOf("A" to listOf("B"), "B" to emptyList(), "C" to emptyList()), "A", "C"),
        case("same node", true, mapOf("A" to emptyList<String>()), "A", "A"),
    ),
    exercise(
        "connectedComponentCount",
        ::connectedComponentCount,
        case("edge and isolated node", 2, mapOf(0 to listOf(1), 1 to listOf(0), 2 to emptyList())),
        case("empty graph", 0, emptyMap<Int, List<Int>>()),
        case("one component", 1, mapOf(0 to listOf(1), 1 to listOf(0, 2), 2 to listOf(1))),
    ),
    exercise(
        "hasDirectedCycle",
        ::hasDirectedCycle,
        case("two-node cycle", true, mapOf("A" to listOf("B"), "B" to listOf("A"))),
        case("directed acyclic graph", false, mapOf("A" to listOf("B", "C"), "B" to listOf("C"), "C" to emptyList())),
        case("self loop", true, mapOf("A" to listOf("A"))),
        case("empty graph", false, emptyMap<String, List<String>>()),
    ),
    exercise(
        "climbingWays",
        ::climbingWays,
        case("zero steps", 1, 0),
        case("one step", 1, 1),
        case("four steps", 5, 4),
    ),
    exercise(
        "maximumNonAdjacentSum",
        ::maximumNonAdjacentSum,
        case("alternating choices", 12, listOf(2, 7, 9, 3, 1)),
        case("empty input", 0, emptyList<Int>()),
        case("both ends", 10, listOf(5, 1, 1, 5)),
        case("all zeroes", 0, listOf(0, 0)),
    ),
    exercise(
        "minimumCoinCount",
        ::minimumCoinCount,
        case("non-greedy optimum", 2, listOf(1, 3, 4), 6),
        case("impossible amount", -1, listOf(2), 3),
        case("zero amount", 0, emptyList<Int>(), 0),
        case("reused coin", 2, listOf(2, 5), 10),
    ),
    exercise(
        "gridPathCount",
        ::gridPathCount,
        case("square grid", 6, 3, 3),
        case("single row", 1, 1, 5),
        case("rectangular grid", 3, 2, 3),
    ),
)

private class Judge(private val exercises: List<ExerciseTests>) {
    val exerciseNames: List<String>
        get() = exercises.map { it.name }

    fun run(selectedNames: Set<String>): Boolean {
        val selected = exercises.filter { selectedNames.isEmpty() || it.name in selectedNames }
        var passedFunctionCount = 0
        var failedFunctionCount = 0
        var skippedFunctionCount = 0
        val detailedOutput = selectedNames.isNotEmpty()
        var reportedExercise = false

        for (exercise in selected) {
            val results = exercise.cases.map { runCase(exercise.function, it) }
            val passedCases = results.count { it.status == CaseStatus.PASSED }
            val failedCases = results.count { it.status == CaseStatus.FAILED }
            val skippedCases = results.count { it.status == CaseStatus.SKIPPED }

            when {
                failedCases > 0 -> failedFunctionCount++
                skippedCases > 0 -> skippedFunctionCount++
                else -> passedFunctionCount++
            }

            when {
                detailedOutput -> {
                    if (reportedExercise) println()
                    println(exercise.name)
                    for (result in results) {
                        val suffix = result.detail.takeIf { it.isNotEmpty() }?.let { ": $it" }.orEmpty()
                        println("  ${result.status.coloredLabel}  ${result.case.name}$suffix")
                    }
                    println(
                        "  Result: ${formatCount(CaseStatus.PASSED, passedCases)}, " +
                            "${formatCount(CaseStatus.FAILED, failedCases)}, " +
                            formatCount(CaseStatus.SKIPPED, skippedCases),
                    )
                    reportedExercise = true
                }
                failedCases > 0 -> {
                    println("${CaseStatus.FAILED.coloredLabel} ${exercise.name}")
                    results.filter { it.status == CaseStatus.FAILED }.forEach { result ->
                        println("  ${result.status.coloredLabel}  ${result.case.name}: ${result.detail}")
                    }
                    reportedExercise = true
                }
                skippedCases == 0 -> {
                    println("${CaseStatus.PASSED.coloredLabel} ${exercise.name}")
                    reportedExercise = true
                }
            }
        }

        if (reportedExercise) println()
        println(
            "Total functions: ${formatCount(CaseStatus.PASSED, passedFunctionCount)}, " +
                "${formatCount(CaseStatus.FAILED, failedFunctionCount)}, " +
                formatCount(CaseStatus.SKIPPED, skippedFunctionCount),
        )
        return failedFunctionCount == 0
    }

    private fun runCase(function: Function<*>, case: TestCase): CaseResult {
        val arguments = case.arguments.map(::deepCopy)
        val originalArguments = arguments.map(::deepCopy)

        val actual = try {
            invoke(function, arguments)
        } catch (error: NotImplementedError) {
            return CaseResult(case, CaseStatus.SKIPPED, error.message ?: "not implemented")
        } catch (error: Exception) {
            return CaseResult(
                case,
                CaseStatus.FAILED,
                "threw ${error::class.simpleName}: ${error.message}",
            )
        }

        if (!case.allowsMutation && arguments != originalArguments) {
            return CaseResult(case, CaseStatus.FAILED, "mutated its input arguments")
        }
        if (actual != case.expected) {
            return CaseResult(case, CaseStatus.FAILED, "expected ${case.expected}, got $actual")
        }
        return CaseResult(case, CaseStatus.PASSED)
    }

    @Suppress("UNCHECKED_CAST")
    private fun invoke(function: Function<*>, arguments: List<Any?>): Any? =
        when (arguments.size) {
            0 -> (function as Function0<Any?>)()
            1 -> (function as Function1<Any?, Any?>)(arguments[0])
            2 -> (function as Function2<Any?, Any?, Any?>)(arguments[0], arguments[1])
            3 -> (function as Function3<Any?, Any?, Any?, Any?>)(arguments[0], arguments[1], arguments[2])
            else -> error("The judge supports functions with at most three arguments")
        }

    private fun deepCopy(value: Any?): Any? = when (value) {
        is List<*> -> value.mapTo(mutableListOf()) { deepCopy(it) }
        is Set<*> -> value.mapTo(linkedSetOf()) { deepCopy(it) }
        is Map<*, *> -> value.entries.associateTo(linkedMapOf()) {
            deepCopy(it.key) to deepCopy(it.value)
        }
        is Pair<*, *> -> deepCopy(value.first) to deepCopy(value.second)
        is ListNode -> value.deepCopy()
        is TreeNode -> value.deepCopy()
        else -> value
    }

    private fun formatCount(status: CaseStatus, count: Int): String =
        "${status.coloredLabel} $count"
}

fun main(arguments: Array<String>) {
    val judge = Judge(exerciseTests)

    if (arguments.contentEquals(arrayOf("--list"))) {
        judge.exerciseNames.forEach(::println)
        return
    }
    if ("--list" in arguments) {
        System.err.println("--list cannot be combined with exercise names")
        kotlin.system.exitProcess(2)
    }

    val requestedNames = arguments.toSet()
    val unknownNames = requestedNames - judge.exerciseNames.toSet()
    if (unknownNames.isNotEmpty()) {
        System.err.println("Unknown exercise name(s): ${unknownNames.sorted().joinToString()}")
        System.err.println("Use --list to see the available names.")
        kotlin.system.exitProcess(2)
    }

    if (!judge.run(requestedNames)) {
        kotlin.system.exitProcess(1)
    }
}
