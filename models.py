from dataclasses import dataclass, field


@dataclass
class VM:
    vm_id: str
    workload: str
    priority: str

    allocated_resources: dict = field(default_factory=dict)
    requested_resources: dict = field(default_factory=dict)

    progress: int = 0
    state: str = "NEW"

    def display(self):
        print(f"\n{self.vm_id}")
        print(f"  Workload : {self.workload}")
        print(f"  Priority : {self.priority}")
        print(f"  Allocated: {self.allocated_resources}")
        print(f"  Requested: {self.requested_resources}")
        print(f"  Progress : {self.progress}%")
        print(f"  State    : {self.state}")