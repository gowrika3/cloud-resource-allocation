from vm_manager import VMManager
from workload_manager import WorkloadManager
from resource_manager import ResourceManager


vm_manager = VMManager()
workload_manager = WorkloadManager()
resource_manager = ResourceManager()


# Create VMs
vm1 = vm_manager.create_vm(
    "VM1",
    "AI Training",
    "HIGH"
)

vm2 = vm_manager.create_vm(
    "VM2",
    "Database",
    "MEDIUM"
)

vm3 = vm_manager.create_vm(
    "VM3",
    "Web Server",
    "MEDIUM"
)


# Allocate resources
for vm in vm_manager.vms:

    resources = workload_manager.get_resource_requirements(
        vm.workload
    )

    resource_manager.allocate_resources(
        vm,
        resources
    )


# Get resource ownership
holders = resource_manager.get_resource_holders(
    vm_manager.vms
)


# Display ownership
print("\n========================================")
print("          RESOURCE OWNERSHIP")
print("========================================")

for resource, owners in holders.items():

    print(f"\n{resource}:")

    for vm_id, amount in owners:

        print(
            f"  {vm_id} holds {amount}"
        )