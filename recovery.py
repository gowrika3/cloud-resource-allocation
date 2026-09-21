class RecoveryEngine:

    def __init__(self):
        self.recovery_history = []

    def recover_vm(self, vm, resource_manager):
        """
        Recover a selected VM by terminating it
        and releasing its allocated resources.
        """

        print("\n========================================")
        print("             VM RECOVERY")
        print("========================================")

        print(
            f"Recovering {vm.vm_id}..."
        )

        # Store information before releasing resources
        released_resources = vm.allocated_resources.copy()

        # Release the VM's allocated resources
        for resource, amount in released_resources.items():

            if resource in resource_manager.allocated_resources:

                resource_manager.allocated_resources[resource] -= amount

        # Clear VM resources
        vm.allocated_resources.clear()

        # Clear any pending request
        vm.requested_resources.clear()

        # Change VM state
        vm.state = "RECOVERED"

        # Store recovery information
        recovery_record = {
            "vm_id": vm.vm_id,
            "released_resources": released_resources
        }

        self.recovery_history.append(
            recovery_record
        )

        print(
            f"{vm.vm_id} recovered successfully."
        )

        print(
            f"Released resources: "
            f"{released_resources}"
        )

        return True

    def display_recovery_history(self):
        """
        Display all recovery actions.
        """

        print("\n========================================")
        print("          RECOVERY HISTORY")
        print("========================================")

        if not self.recovery_history:

            print("No recovery actions yet.")
            return

        for record in self.recovery_history:

            print(
                f"{record['vm_id']} -> "
                f"Released: "
                f"{record['released_resources']}"
            )