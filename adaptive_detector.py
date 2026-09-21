class AdaptiveDetector:

    def __init__(self):

        self.selected_algorithm = None
        self.complexity_score = 0

        # Prototype threshold
        self.threshold = 2.5

    def calculate_complexity(self, dependencies):
        """
        Calculate dependency complexity.

        N = number of VMs
        E = number of dependency edges

        Complexity =
            (E / N) + (E / (N * (N - 1)))
        """

        number_of_vms = len(dependencies)

        number_of_edges = 0

        for vm_id, dependent_vms in dependencies.items():

            number_of_edges += len(dependent_vms)

        # Avoid division by zero
        if number_of_vms <= 1:
            return 0

        complexity = (
            (number_of_edges / number_of_vms)
            +
            (
                number_of_edges
                /
                (
                    number_of_vms
                    * (number_of_vms - 1)
                )
            )
        )

        return complexity

    def choose_algorithm(self, dependencies):
        """
        Select the detection algorithm based
        on dependency graph complexity.

        Low complexity  -> Wait-for Graph
        High complexity -> Probe
        """

        self.complexity_score = (
            self.calculate_complexity(
                dependencies
            )
        )

        if self.complexity_score < self.threshold:

            self.selected_algorithm = (
                "WAIT_FOR_GRAPH"
            )

        else:

            self.selected_algorithm = "PROBE"

        return self.selected_algorithm

    def display_selection(self):

        print("\n========================================")
        print("       ADAPTIVE DETECTION")
        print("========================================")

        print(
            f"Dependency complexity: "
            f"{self.complexity_score:.2f}"
        )

        print(
            f"Threshold: "
            f"{self.threshold}"
        )

        print(
            f"Selected algorithm: "
            f"{self.selected_algorithm}"
        )