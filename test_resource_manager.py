from models import VM
from resource_manager import ResourceManager


# Create resource manager
resource_manager = ResourceManager()

# Create a VM
vm1 = VM(
    vm_id="VM1",
    workload="AI Training",
    priority="HIGH"
)

# VM requests resources
request = {
    "CPU": 4,
    "RAM": 8,
    "Storage": 20,
    "GPU": 1
}

print("\nVM1 requesting resources:")
print(request)

# Try allocation
if resource_manager.allocate_resources(vm1, request):
    print("Allocation successful.")
else:
    print("Allocation failed.")

# Display VM information
vm1.display()

# Display cloud resources
resource_manager.display_resources()