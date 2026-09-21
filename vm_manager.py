from models import VM


class VMManager:

    def __init__(self):
        self.vms = []

    def create_vm(self, vm_id, workload, priority):
        vm = VM(
            vm_id=vm_id,
            workload=workload,
            priority=priority
        )

        self.vms.append(vm)

        print(f"Created {vm_id} - {workload} - Priority: {priority}")

        return vm

    def display_all_vms(self):
        print("\n========================================")
        print("           VIRTUAL MACHINES")
        print("========================================")

        for vm in self.vms:
            vm.display()


if __name__ == "__main__":

    manager = VMManager()

    manager.create_vm("VM1", "AI Training", "HIGH")
    manager.create_vm("VM2", "Database", "MEDIUM")
    manager.create_vm("VM3", "Backup", "LOW")
    manager.create_vm("VM4", "Web Server", "MEDIUM")

    manager.display_all_vms()