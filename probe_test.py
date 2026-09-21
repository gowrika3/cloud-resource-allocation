from dependency_analyzer import DependencyAnalyzer
from deadlock_detector import DeadlockDetector


# ----------------------------------------
# COMPLEX DEPENDENCY SCENARIO
# ----------------------------------------

dependencies = {
    "VM1": ["VM2"],
    "VM2": ["VM3"],
    "VM3": ["VM4"],
    "VM4": ["VM1"]
}


# ----------------------------------------
# DEPENDENCY ANALYSIS
# ----------------------------------------

analyzer = DependencyAnalyzer()

analyzer.dependencies = dependencies

analyzer.display_dependencies()


# ----------------------------------------
# DEADLOCK DETECTION
# ----------------------------------------

detector = DeadlockDetector()

deadlock = detector.detect(
    dependencies
)

detector.display_result()


# ----------------------------------------
# FINAL RESULT
# ----------------------------------------

print("\n========================================")

if deadlock:

    print("PROBE TEST: DEADLOCK DETECTED")

else:

    print("PROBE TEST: NO DEADLOCK")

print("========================================")