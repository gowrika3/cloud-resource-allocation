from models import VM
from waiting_queue import WaitingQueue


# Create waiting queue
waiting_queue = WaitingQueue()

# Create VM
vm2 = VM(
    vm_id="VM2",
    workload="Database",
    priority="MEDIUM"
)

# Resources requested by VM2
request = {
    "GPU": 1
}

# Add VM to waiting queue
waiting_queue.add_vm(vm2, request)

# Display queue
waiting_queue.display_queue()