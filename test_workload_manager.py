from workload_manager import WorkloadManager


workload_manager = WorkloadManager()


# Test AI Training
ai_resources = workload_manager.get_resource_requirements(
    "AI Training"
)

print("\nAI Training requires:")
print(ai_resources)


# Test Database
database_resources = workload_manager.get_resource_requirements(
    "Database"
)

print("\nDatabase requires:")
print(database_resources)


# Display all workloads
workload_manager.display_workloads()