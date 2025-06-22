from graph_manager import RAGraph

# Create graph manager object
rag = RAGraph()

# Add processes and resources
rag.add_process('P1')
rag.add_process('P2')
rag.add_resource('R1')
rag.add_resource('R2')

# Create edges
rag.request_edge('P1', 'R1')
rag.assign_edge('R1', 'P2')
rag.request_edge('P2', 'R2')
rag.assign_edge('R2', 'P1')  # This creates a cycle: P1 → R1 → P2 → R2 → P1

# Detect deadlock
cycles = rag.detect_deadlock()
if cycles:
    print("⚠️ Deadlock detected! Cycle(s):")
    for cycle in cycles:
        print(" -> ".join(cycle))
else:
    print("✅ No deadlock detected.")
