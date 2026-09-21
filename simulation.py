from vm_manager import VMManager
from workload_manager import WorkloadManager
from resource_manager import ResourceManager

from dependency_analyzer import DependencyAnalyzer
from deadlock_detector import DeadlockDetector
from ris import RecoveryImpactScore
from recovery import RecoveryEngine


class CloudSimulation:

    def __init__(self):

        # Core cloud modules
        self.vm_manager = VMManager()
        self.workload_manager = WorkloadManager()
        self.resource_manager = ResourceManager()

        # Deadlock management modules
        self.dependency_analyzer = DependencyAnalyzer()
        self.deadlock_detector = DeadlockDetector()
        self.ris = RecoveryImpactScore()
        self.recovery_engine = RecoveryEngine()

    # ========================================
    # 1. VM CREATION
    # ========================================

    def setup_vms(self):

        print("\n[1] VM CREATION")
        print("----------------------------------------")

        self.vm1 = self.vm_manager.create_vm(
            "VM1",
            "AI Training",
            "HIGH"
        )

        self.vm2 = self.vm_manager.create_vm(
            "VM2",
            "Database",
            "MEDIUM"
        )

    # ========================================
    # 2. RESOURCE ALLOCATION
    # ========================================

    def create_deadlock_scenario(self):

        print("\n[2] RESOURCE ALLOCATION")
        print("----------------------------------------")

        # VM1 receives CPU
        self.resource_manager.allocate_resources(
            self.vm1,
            {
                "CPU": 4
            }
        )

        # VM2 receives RAM
        self.resource_manager.allocate_resources(
            self.vm2,
            {
                "RAM": 8
            }
        )

        print("\nCurrent allocation:")

        print(
            f"  {self.vm1.vm_id}: "
            f"{self.vm1.allocated_resources}"
        )

        print(
            f"  {self.vm2.vm_id}: "
            f"{self.vm2.allocated_resources}"
        )

        # ========================================
        # 3. DYNAMIC RESOURCE REQUESTS
        # ========================================

        print("\n[3] DYNAMIC RESOURCE REQUESTS")
        print("----------------------------------------")

        # VM1 requests RAM
        self.vm1.requested_resources = {
            "RAM": 4
        }

        self.vm1.state = "WAITING"

        self.resource_manager.waiting_queue.add_vm(
            self.vm1,
            self.vm1.requested_resources
        )

        print(
            "  VM1 → Waiting for RAM"
        )

        # VM2 requests CPU
        self.vm2.requested_resources = {
            "CPU": 2
        }

        self.vm2.state = "WAITING"

        self.resource_manager.waiting_queue.add_vm(
            self.vm2,
            self.vm2.requested_resources
        )

        print(
            "  VM2 → Waiting for CPU"
        )

    # ========================================
    # 4. DEPENDENCY ANALYSIS
    # ========================================

    def analyze_dependencies(self):

        print("\n[4] DEPENDENCY ANALYSIS")
        print("----------------------------------------")

        dependencies = (
            self.dependency_analyzer.analyze(
                self.vm_manager.vms
            )
        )

        self.dependency_analyzer.display_dependencies()

        return dependencies

    # ========================================
    # 5. ADAPTIVE DEADLOCK DETECTION
    # ========================================

    def detect_deadlock(self, dependencies):

        print("\n[5] ADAPTIVE DEADLOCK DETECTION")
        print("----------------------------------------")

        deadlock = (
            self.deadlock_detector.detect(
                dependencies
            )
        )

        self.deadlock_detector.display_result()

        return deadlock

    # ========================================
    # 6. RIS + RECOVERY
    # ========================================

    def perform_recovery(self):

        print("\n[6] RECOVERY IMPACT ANALYSIS")
        print("----------------------------------------")

        # Calculate RIS
        self.ris.calculate_for_vms(
            self.vm_manager.vms
        )

        self.ris.display_scores()

        # Select recovery candidate
        selected_vm_id = (
            self.ris.select_recovery_vm()
        )

        print(
            f"\nRecovery candidate: "
            f"{selected_vm_id}"
        )

        # Find selected VM
        selected_vm = None

        for vm in self.vm_manager.vms:

            if vm.vm_id == selected_vm_id:

                selected_vm = vm
                break

        if selected_vm is None:

            print("No recovery candidate found.")
            return

        # Recover selected VM
        self.recovery_engine.recover_vm(
            selected_vm,
            self.resource_manager
        )

        # Remove recovered VM from queue
        self.resource_manager.waiting_queue.remove_vm(
            selected_vm
        )

        # ========================================
        # 7. PROCESS WAITING QUEUE
        # ========================================

        print("\n[7] WAITING QUEUE RESUMPTION")
        print("----------------------------------------")

        self.resource_manager.process_waiting_queue()

        self.recovery_engine.display_recovery_history()

    # ========================================
    # 8. FINAL SYSTEM STATE
    # ========================================

    def display_final_state(self):

        print("\n[8] FINAL SYSTEM STATE")
        print("----------------------------------------")

        self.vm_manager.display_all_vms()

        self.resource_manager.display_resources()

        self.resource_manager.waiting_queue.display_queue()

    # ========================================
    # COMPLETE SIMULATION
    # ========================================

    def run(self):

        print("\n")
        print("========================================")
        print(" CLOUD RESOURCE ALLOCATION &")
        print(" DEADLOCK PREVENTION SYSTEM")
        print("========================================")

        print(
            "\nStarting cloud simulation..."
        )

        # VM creation
        self.setup_vms()

        # Resource allocation + deadlock scenario
        self.create_deadlock_scenario()

        # Dependency analysis
        dependencies = (
            self.analyze_dependencies()
        )

        # Deadlock detection
        deadlock = (
            self.detect_deadlock(
                dependencies
            )
        )

        # Recovery
        if deadlock:

            self.perform_recovery()

        # Final state
        self.display_final_state()

        print("\n========================================")
        print("       SIMULATION COMPLETED")
        print("========================================")


# ========================================
# PROGRAM START
# ========================================

if __name__ == "__main__":

    simulation = CloudSimulation()

    simulation.run()