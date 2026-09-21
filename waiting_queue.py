class WaitingQueue:

    def __init__(self):
        self.queue = []

    def add_vm(self, vm, requested_resources):
        """
        Add a VM to the waiting queue.
        """

        vm.requested_resources = requested_resources
        vm.state = "WAITING"

        self.queue.append(vm)

        print(f"\n{vm.vm_id} added to waiting queue.")
        print(f"Waiting for: {requested_resources}")

    def remove_vm(self, vm):
        """
        Remove a VM from the waiting queue.
        """

        if vm in self.queue:
            self.queue.remove(vm)

    def get_waiting_vms(self):
        """
        Return all VMs currently waiting.
        """

        return self.queue

    def display_queue(self):
        """
        Display the current waiting queue.
        """

        print("\n========================================")
        print("             WAITING QUEUE")
        print("========================================")

        if not self.queue:
            print("Queue is empty.")
            return

        for vm in self.queue:
            print(
                f"{vm.vm_id} | "
                f"Workload: {vm.workload} | "
                f"Waiting for: {vm.requested_resources}"
            )