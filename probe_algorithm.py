class ProbeAlgorithm:

    def __init__(self):
        self.detected_cycle = []

    def detect_cycle(self, graph):
        """
        Detect a cycle in the Wait-for Graph
        using a probe-based traversal.

        Returns:
            True  -> cycle detected
            False -> no cycle detected
        """

        self.detected_cycle = []

        for start_vm in graph:

            visited = set()
            path = []

            if self._probe(
                start_vm,
                start_vm,
                graph,
                visited,
                path
            ):
                return True

        return False

    def _probe(
        self,
        current_vm,
        start_vm,
        graph,
        visited,
        path
    ):
        """
        Recursively send a probe through dependent VMs.
        """

        # Add current VM to the current path
        path.append(current_vm)

        # A probe has returned to its starting VM
        # which means a cycle exists.
        if (
            current_vm == start_vm
            and len(path) > 1
        ):
            self.detected_cycle = path.copy()
            return True

        # Avoid repeatedly exploring the same VM
        if current_vm in visited:
            path.pop()
            return False

        visited.add(current_vm)

        # Follow all outgoing dependency edges
        for next_vm in graph.get(current_vm, []):

            # If the next VM is the starting VM,
            # a cycle has been found.
            if next_vm == start_vm:

                self.detected_cycle = (
                    path + [next_vm]
                )

                return True

            if self._probe(
                next_vm,
                start_vm,
                graph,
                visited,
                path
            ):
                return True

        path.pop()

        return False

    def get_cycle(self):
        """
        Return the detected cycle.
        """

        return self.detected_cycle

    def display_result(self):
        """
        Display the probe algorithm result.
        """

        print("\n========================================")
        print("          PROBE ALGORITHM")
        print("========================================")

        if self.detected_cycle:

            print("Deadlock cycle detected:")

            print(
                " -> ".join(self.detected_cycle)
            )

        else:

            print("No deadlock cycle detected.")