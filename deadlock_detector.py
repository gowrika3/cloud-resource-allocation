from wait_for_graph import WaitForGraph
from probe_algorithm import ProbeAlgorithm
from adaptive_detector import AdaptiveDetector


class DeadlockDetector:

    def __init__(self):

        self.wait_for_graph = WaitForGraph()
        self.probe_algorithm = ProbeAlgorithm()
        self.adaptive_detector = AdaptiveDetector()

        self.deadlock_detected = False
        self.deadlock_cycle = []
        self.selected_algorithm = None

    def detect(self, dependencies):
        """
        Detect deadlock using adaptive algorithm selection.

        The Adaptive Detector first selects the detection
        approach based on the dependency structure.
        """

        # ----------------------------------------
        # STEP 1: Select detection algorithm
        # ----------------------------------------

        self.selected_algorithm = (
            self.adaptive_detector.choose_algorithm(
                dependencies
            )
        )

        self.adaptive_detector.display_selection()

        # ----------------------------------------
        # STEP 2: Build the Wait-for Graph
        # ----------------------------------------

        graph = self.wait_for_graph.build_graph(
            dependencies
        )

        # ----------------------------------------
        # STEP 3: Detect using selected approach
        # ----------------------------------------

        if self.selected_algorithm == "WAIT_FOR_GRAPH":

            self.deadlock_detected = (
                self.detect_cycle_using_graph(graph)
            )

        else:

            self.deadlock_detected = (
                self.probe_algorithm.detect_cycle(
                    graph
                )
            )

        # ----------------------------------------
        # STEP 4: Store detected cycle
        # ----------------------------------------

        self.deadlock_cycle = (
            self.probe_algorithm.get_cycle()
        )

        return self.deadlock_detected

    def detect_cycle_using_graph(self, graph):
        """
        Detect a cycle directly using DFS
        on the Wait-for Graph.
        """

        visited = set()
        recursion_stack = set()

        for vm in graph:

            if vm not in visited:

                if self._dfs(
                    vm,
                    graph,
                    visited,
                    recursion_stack
                ):

                    return True

        return False

    def _dfs(
        self,
        current_vm,
        graph,
        visited,
        recursion_stack
    ):
        """
        Depth-first search for cycle detection.
        """

        visited.add(current_vm)
        recursion_stack.add(current_vm)

        for next_vm in graph.get(
            current_vm,
            []
        ):

            if next_vm not in visited:

                if self._dfs(
                    next_vm,
                    graph,
                    visited,
                    recursion_stack
                ):

                    return True

            elif next_vm in recursion_stack:

                self.deadlock_cycle = [
                    current_vm,
                    next_vm
                ]

                return True

        recursion_stack.remove(current_vm)

        return False

    def get_deadlock_cycle(self):
        """
        Return the detected deadlock cycle.
        """

        return self.deadlock_cycle

    def display_result(self):
        """
        Display the final deadlock detection result.
        """

        print("\n========================================")
        print("          DEADLOCK DETECTION")
        print("========================================")

        if self.deadlock_detected:

            print("DEADLOCK DETECTED")

            if self.deadlock_cycle:

                print(
                    "Cycle: "
                    + " -> ".join(
                        self.deadlock_cycle
                    )
                )

        else:

            print("No deadlock detected.")