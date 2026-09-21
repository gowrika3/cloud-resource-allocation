class DependencyAnalyzer:

    def __init__(self):
        self.dependencies = {}

    def analyze(self, vms):
        """
        Analyze dependencies between VMs.

        A dependency exists when a VM is waiting for a
        resource that is currently held by another VM.
        """

        self.dependencies = {}

        for vm in vms:

            # Only waiting VMs can currently have dependencies
            if vm.state != "WAITING":
                continue

            self.dependencies[vm.vm_id] = []

            # Check every resource the VM is waiting for
            for requested_resource in vm.requested_resources:

                # Find VMs holding this resource
                for other_vm in vms:

                    # Do not create a dependency on itself
                    if other_vm.vm_id == vm.vm_id:
                        continue

                    held_amount = other_vm.allocated_resources.get(
                        requested_resource,
                        0
                    )

                    if held_amount > 0:

                        if other_vm.vm_id not in self.dependencies[vm.vm_id]:

                            self.dependencies[vm.vm_id].append(
                                other_vm.vm_id
                            )

        return self.dependencies

    def display_dependencies(self):
        """
        Display the dependency relationships.
        """

        print("\n========================================")
        print("          VM DEPENDENCIES")
        print("========================================")

        if not self.dependencies:
            print("No dependencies found.")
            return

        for vm_id, dependencies in self.dependencies.items():

            if dependencies:

                print(
                    f"{vm_id} depends on: "
                    f"{', '.join(dependencies)}"
                )

            else:

                print(
                    f"{vm_id} has no dependencies."
                )