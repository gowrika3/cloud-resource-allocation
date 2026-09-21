from dependency_analyzer import DependencyAnalyzer
from deadlock_detector import DeadlockDetector


# ----------------------------------------
# STEP 1: Create a test dependency
# ----------------------------------------

dependencies = {
    "VM1": ["VM2"],
    "VM2": ["VM1"]
}


# ----------------------------------------
# STEP 2: Analyze dependencies
# ----------------------------------------

analyzer = DependencyAnalyzer()

result = analyzer.analyze([])

# For this test, we already know the
# dependency relationships.
analyzer.dependencies = dependencies

analyzer.display_dependencies()


# ----------------------------------------
# STEP 3: Build and display
#          the Wait-for Graph
# ----------------------------------------

detector = DeadlockDetector()

detector.wait_for_graph.build_graph(
    dependencies
)

detector.wait_for_graph.display_graph()


# ----------------------------------------
# STEP 4: Detect deadlock
# ----------------------------------------

deadlock = detector.detect(
    dependencies
)

detector.display_result()


# ----------------------------------------
# STEP 5: Display final result
# ----------------------------------------

print("\n========================================")

if deadlock:
    print("TEST RESULT: DEADLOCK DETECTED")
else:
    print("TEST RESULT: NO DEADLOCK")

print("========================================")