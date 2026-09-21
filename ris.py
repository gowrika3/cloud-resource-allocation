class RecoveryImpactScore:

    def __init__(self):
        self.scores = {}

    def calculate_score(
        self,
        execution_progress,
        workload_priority,
        resource_importance
    ):
        """
        Calculate the Recovery Impact Score (RIS).

        Lower RIS means the VM has lower recovery impact
        and is therefore a better candidate for recovery.
        """

        # Convert priority into numerical values
        priority_values = {
            "LOW": 1,
            "MEDIUM": 2,
            "HIGH": 3
        }

        priority_score = priority_values.get(
            workload_priority,
            1
        )

        # Calculate RIS
        score = (
            execution_progress
            + (priority_score * 20)
            + (resource_importance * 10)
        )

        return score

    def calculate_for_vms(self, vms):
        """
        Calculate RIS for all VMs involved in a deadlock.
        """

        self.scores = {}

        for vm in vms:

            score = self.calculate_score(
                vm.progress,
                vm.priority,
                len(vm.allocated_resources)
            )

            self.scores[vm.vm_id] = score

        return self.scores

    def select_recovery_vm(self):
        """
        Select the VM with the lowest RIS
        for recovery.
        """

        if not self.scores:
            return None

        selected_vm = min(
            self.scores,
            key=self.scores.get
        )

        return selected_vm

    def display_scores(self):
        """
        Display RIS values for the VMs.
        """

        print("\n========================================")
        print("       RECOVERY IMPACT SCORES")
        print("========================================")

        if not self.scores:
            print("No RIS values calculated.")
            return

        for vm_id, score in self.scores.items():

            print(
                f"{vm_id:<10} RIS: {score}"
            )