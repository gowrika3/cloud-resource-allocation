class WaitForGraph:

    def __init__(self):
        # Graph format:
        # VM1 -> [VM2, VM3]
        self.graph = {}

    def build_graph(self, dependencies):
        """
        Build a Wait-for Graph from the dependency information.

        Example:
        {
            "VM1": ["VM2"],
            "VM2": ["VM3"]
        }

        means:

        VM1 is waiting for VM2
        VM2 is waiting for VM3
        """

        self.graph = {}

        for vm_id, dependent_vms in dependencies.items():

            self.graph[vm_id] = []

            for other_vm in dependent_vms:

                self.graph[vm_id].append(other_vm)

                # Make sure the other VM also exists
                # as a node in the graph.
                if other_vm not in self.graph:

                    self.graph[other_vm] = []

        return self.graph

    def display_graph(self):
        """
        Display the Wait-for Graph.
        """

        print("\n========================================")
        print("             WAIT-FOR GRAPH")
        print("========================================")

        if not self.graph:

            print("Graph is empty.")
            return

        for vm_id, waiting_for in self.graph.items():

            if waiting_for:

                print(
                    f"{vm_id} -> "
                    f"{', '.join(waiting_for)}"
                )

            else:

                print(
                    f"{vm_id} -> None"
                )

    def get_graph(self):
        """
        Return the current graph.
        """

        return self.graph