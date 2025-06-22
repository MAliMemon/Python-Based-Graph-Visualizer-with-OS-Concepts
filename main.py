from logic.graph_manager import RAGraph
from visualizer.visualizer import draw_graph
from gui.gui import launch_gui

def main():
    rag = RAGraph()

    while True:
        print("\n--- Resource Allocation Graph Manager ---")
        print("1. Add Process")
        print("2. Add Resource")
        print("3. Request Resource")
        print("4. Assign Resource")
        print("5. Detect Deadlock")
        print("6. Draw Graph")
        print("7. Launch GUI")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            pid = input("Enter Process ID: ")
            rag.add_process(pid)

        elif choice == '2':
            rid = input("Enter Resource ID: ")
            rag.add_resource(rid)

        elif choice == '3':
            pid = input("Enter Process ID: ")
            rid = input("Enter Resource ID: ")
            rag.request_edge(pid, rid)

        elif choice == '4':
            rid = input("Enter Resource ID: ")
            pid = input("Enter Process ID: ")
            rag.assign_edge(rid, pid)

        elif choice == '5':
            cycles = rag.detect_deadlock()
            if cycles:
                print("Deadlock detected involving:", cycles)
            else:
                print("No deadlock detected.")

        elif choice == '6':
            draw_graph(rag.graph)

        elif choice == '7':
            launch_gui(rag)

        elif choice == '8':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
