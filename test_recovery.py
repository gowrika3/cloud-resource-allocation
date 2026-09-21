from models import VM
from resource_manager import ResourceManager
from ris import RecoveryImpactScore
from recovery import RecoveryEngine


# ----------------------------------------
# STEP 1: Create test VMs
# ----------------------------------------

vm1 = VM(
    vm_id="VM1",
    workload="AI Training",
    priority="HIGH"
)

vm2 = VM(
    vm_id="VM2",
    workload="Database",
    priority="MEDIUM"
)


# Give the VMs some allocated resources
vm1.allocated_resources = {
    "CPU": 4,
    "RAM": 8
}

vm2.allocated_resources = {
    "CPU": 2,
    "RAM": 6
}


# Give them different execution progress
vm1.progress = 70
vm2.progress = 20


# ----------------------------------------
# STEP 2: Create Resource Manager
# ----------------------------------------

resource_manager = ResourceManager()

resource_manager.allocated_resources = {
    "CPU": 6,
    "RAM": 14,
    "Storage": 0,
    "GPU": 0
}


# ----------------------------------------
# STEP 3: Calculate RIS
# ----------------------------------------

ris = RecoveryImpactScore()

scores = ris.calculate_for_vms(
    [vm1, vm2]
)

ris.display_scores()


# ----------------------------------------
# STEP 4: Select recovery VM
# ----------------------------------------

selected_vm = ris.select_recovery_vm()

print("\n========================================")
print("        RECOVERY SELECTION")
print("========================================")

print(
    f"Selected VM for recovery: {selected_vm}"
)


# ----------------------------------------
# STEP 5: Recover selected VM
# ----------------------------------------

recovery = RecoveryEngine()

if selected_vm == vm1.vm_id:

    recovery.recover_vm(
        vm1,
        resource_manager
    )

else:

    recovery.recover_vm(
        vm2,
        resource_manager
    )


# ----------------------------------------
# STEP 6: Display final resources
# ----------------------------------------

print("\n========================================")
print("       RESOURCES AFTER RECOVERY")
print("========================================")

print(
    resource_manager.allocated_resources
)

recovery.display_recovery_history()