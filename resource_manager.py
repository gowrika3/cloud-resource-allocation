from waiting_queue import WaitingQueue


class ResourceManager:

    def __init__(self):

        # Total resources available in the cloud
        self.total_resources = {
            "CPU": 16,
            "RAM": 32,
            "Storage": 100,
            "GPU": 2
        }

        # Resources currently allocated to VMs
        self.allocated_resources = {
            "CPU": 0,
            "RAM": 0,
            "Storage": 0,
            "GPU": 0
        }

        # Waiting queue
        self.waiting_queue = WaitingQueue()

    def get_available_resources(self):
        """Calculate currently available resources."""

        available = {}

        for resource in self.total_resources:

            available[resource] = (
                self.total_resources[resource]
                - self.allocated_resources[resource]
            )

        return available

    def can_allocate(self, requested_resources):
        """Check whether enough resources are available."""

        available = self.get_available_resources()

        for resource, amount in requested_resources.items():

            if resource not in available:

                print(f"Unknown resource: {resource}")
                return False

            if amount > available[resource]:

                return False

        return True

    def allocate_resources(self, vm, requested_resources):
        """
        Allocate resources to a VM if available.
        Otherwise, add the VM to the waiting queue.
        """

        if not self.can_allocate(requested_resources):

            print(
                f"\nResources unavailable for {vm.vm_id}"
            )

            self.waiting_queue.add_vm(
                vm,
                requested_resources
            )

            return False

        # Allocate resources
        for resource, amount in requested_resources.items():

            self.allocated_resources[resource] += amount

            vm.allocated_resources[resource] = (
                vm.allocated_resources.get(resource, 0)
                + amount
            )

        # Request fulfilled
        vm.requested_resources = {}

        # VM can run
        vm.state = "RUNNING"

        print(
            f"\nResources allocated successfully to {vm.vm_id}"
        )

        return True

    def process_waiting_queue(self):
        """
        Check waiting VMs and try to allocate their
        requested resources again.

        This is called after resources are released
        during recovery.
        """

        print("\n========================================")
        print("       PROCESSING WAITING QUEUE")
        print("========================================")

        if not self.waiting_queue.queue:

            print("Waiting queue is empty.")
            return

        # Use a copy because VMs may be removed
        # from the actual queue while processing.
        waiting_vms = self.waiting_queue.queue.copy()

        for vm in waiting_vms:

            requested_resources = (
                vm.requested_resources.copy()
            )

            print(
                f"\nChecking {vm.vm_id}..."
            )

            print(
                f"Requested: {requested_resources}"
            )

            if self.can_allocate(
                requested_resources
            ):

                # Remove from waiting queue first
                self.waiting_queue.remove_vm(vm)

                # Allocate resources directly
                for resource, amount in requested_resources.items():

                    self.allocated_resources[resource] += amount

                    vm.allocated_resources[resource] = (
                        vm.allocated_resources.get(
                            resource,
                            0
                        )
                        + amount
                    )

                # Request fulfilled
                vm.requested_resources = {}

                # VM resumes execution
                vm.state = "RUNNING"

                print(
                    f"{vm.vm_id} can now resume."
                )

                print(
                    f"Allocated: "
                    f"{vm.allocated_resources}"
                )

            else:

                print(
                    f"{vm.vm_id} still has to wait."
                )

    def get_resource_holders(self, vms):
        """
        Find which VM currently holds each resource.
        """

        resource_holders = {}

        for vm in vms:

            for resource, amount in (
                vm.allocated_resources.items()
            ):

                if amount > 0:

                    if resource not in resource_holders:

                        resource_holders[resource] = []

                    resource_holders[resource].append(
                        (vm.vm_id, amount)
                    )

        return resource_holders

    def display_resources(self):
        """Display total, allocated and available resources."""

        available = self.get_available_resources()

        print("\n========================================")
        print("          CLOUD RESOURCE STATUS")
        print("========================================")

        for resource in self.total_resources:

            print(
                f"{resource:<10} "
                f"Total: {self.total_resources[resource]:<4} "
                f"Allocated: {self.allocated_resources[resource]:<4} "
                f"Available: {available[resource]}"
            )