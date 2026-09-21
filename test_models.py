from models import VM


vm1 = VM(
    vm_id="VM1",
    workload="AI Training",
    priority="HIGH"
)

vm1.allocated_resources = {
    "CPU": 2,
    "RAM": 4,
    "Storage": 20,
    "GPU": 1
}

vm1.requested_resources = {
    "CPU": 2,
    "RAM": 4
}

vm1.progress = 25
vm1.state = "RUNNING"

vm1.display()