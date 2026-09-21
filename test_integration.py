from models import VM
from resource_manager import ResourceManager


# Create the resource manager
resource_manager = ResourceManager()


# -------------------------------
# VM1 gets resources successfully
# -------------------------------

vm1 = VM(
    vm_id="VM1",
    workload="AI Training",
    priority="HIGH"
)

request1 = {
    "CPU": 4,
    "RAM": 8,
    "Storage": 20,
    "GPU": 1
}

print("\n========== VM1 RESOURCE REQUEST ==========")
print(request1)

resource_manager.allocate_resources(vm1, request1)


# -------------------------------
# VM2 requests the remaining GPU
# -------------------------------

vm2 = VM(
    vm_id="VM2",
    workload="Database",
    priority="MEDIUM"
)

request2 = {
    "CPU": 4,
    "RAM": 8,
    "Storage": 20,
    "GPU": 1
}

print("\n========== VM2 RESOURCE REQUEST ==========")
print(request2)

resource_manager.allocate_resources(vm2, request2)


# -------------------------------
# VM3 requests GPU when none is available
# -------------------------------

vm3 = VM(
    vm_id="VM3",
    workload="Backup",
    priority="LOW"
)

request3 = {
    "CPU": 2,
    "RAM": 4,
    "GPU": 1
}

print("\n========== VM3 RESOURCE REQUEST ==========")
print(request3)

resource_manager.allocate_resources(vm3, request3)


# -------------------------------
# Display final resource status
# -------------------------------

resource_manager.display_resources()


# -------------------------------
# Display waiting queue
# -------------------------------

resource_manager.waiting_queue.display_queue()


# -------------------------------
# Display VM3 status
# -------------------------------

print("\n========== VM3 STATUS ==========")
vm3.display()