class WorkloadManager:

    def __init__(self):
        # Resource requirements for each workload type
        self.workloads = {
            "AI Training": {
                "CPU": 6,
                "RAM": 12,
                "Storage": 20,
                "GPU": 1
            },

            "Database": {
                "CPU": 4,
                "RAM": 10,
                "Storage": 30,
                "GPU": 0
            },

            "Backup": {
                "CPU": 2,
                "RAM": 4,
                "Storage": 60,
                "GPU": 0
            },

            "Web Server": {
                "CPU": 3,
                "RAM": 6,
                "Storage": 10,
                "GPU": 0
            }
        }

    def get_resource_requirements(self, workload):
        """
        Return the resource requirements for a workload.
        """

        if workload not in self.workloads:
            print(f"Unknown workload: {workload}")
            return None

        return self.workloads[workload].copy()

    def display_workloads(self):
        """
        Display all available workloads and their requirements.
        """

        print("\n========================================")
        print("          WORKLOAD PROFILES")
        print("========================================")

        for workload, resources in self.workloads.items():

            print(f"\n{workload}")

            for resource, amount in resources.items():
                print(f"  {resource:<10}: {amount}")