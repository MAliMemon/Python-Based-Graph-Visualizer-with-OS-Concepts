import networkx as nx

class RAGraph:
    def __init__(self):
        # Directed graph for RAG
        self.graph = nx.DiGraph()
    
    def add_process(self, process_id):
        """Add a process node."""
        self.graph.add_node(process_id, type='process')
    
    def add_resource(self, resource_id):
        """Add a resource node."""
        self.graph.add_node(resource_id, type='resource')
    
    def request_edge(self, process_id, resource_id):
        """Add a request edge from process to resource."""
        self.graph.add_edge(process_id, resource_id, type='request')
    
    def assign_edge(self, resource_id, process_id):
        """Add an allocation edge from resource to process."""
        self.graph.add_edge(resource_id, process_id, type='allocation')
    
    def detect_deadlock(self):
        """Detect deadlock using cycle detection."""
        try:
            cycles = list(nx.simple_cycles(self.graph))
            if cycles:
                return cycles  #return all cycles (if deadlocks)
            return None  #no deadlock
        except Exception as e:
            print(f"Error detecting deadlock: {e}")
            return None