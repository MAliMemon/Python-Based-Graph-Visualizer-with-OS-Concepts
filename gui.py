import tkinter as tk
from tkinter import messagebox
from logic.graph_manager import RAGraph
from visualizer.visualizer import draw_graph

def launch_gui(rag):
    root = tk.Tk()
    root.title("Resource Allocation Graph - Deadlock Detection")
    root.geometry("920x720")
    root.configure(bg="#000000")  # jet black background

    # Style settings
    entry_bg = "#1a1a1a"
    entry_fg = "white"
    button_bg = "#ffffff"
    button_fg = "#000000"
    font_family = ("Segoe UI", 11)

    # Title Label
    title_label = tk.Label(
        root, 
        text="Resource Allocation Graph Manager", 
        bg="#000000", 
        fg="#ffffff", 
        font=("Segoe UI", 18, "bold")
    )
    title_label.pack(pady=20)

    # Input Frame
    input_frame = tk.Frame(root, bg="#000000")
    input_frame.pack(pady=10)

    process_label = tk.Label(input_frame, text="Process ID:", bg="#000000", fg="white", font=font_family)
    process_label.grid(row=0, column=0, padx=5, pady=5)
    process_entry = tk.Entry(input_frame, width=25, bg=entry_bg, fg=entry_fg, font=font_family)
    process_entry.grid(row=0, column=1, padx=5, pady=5)

    resource_label = tk.Label(input_frame, text="Resource ID:", bg="#000000", fg="white", font=font_family)
    resource_label.grid(row=1, column=0, padx=5, pady=5)
    resource_entry = tk.Entry(input_frame, width=25, bg=entry_bg, fg=entry_fg, font=font_family)
    resource_entry.grid(row=1, column=1, padx=5, pady=5)

    # Action Functions
    def add_process():
        pid = process_entry.get()
        if pid:
            rag.add_process(pid)
            draw_graph(rag.graph)
        else:
            messagebox.showerror("Error", "Please enter a Process ID")

    def add_resource():
        rid = resource_entry.get()
        if rid:
            rag.add_resource(rid)
            draw_graph(rag.graph)
        else:
            messagebox.showerror("Error", "Please enter a Resource ID")

    def request_resource():
        pid = process_entry.get()
        rid = resource_entry.get()
        if pid and rid:
            rag.request_edge(pid, rid)
            draw_graph(rag.graph)
        else:
            messagebox.showerror("Error", "Please enter both Process and Resource IDs")

    def assign_resource():
        rid = resource_entry.get()
        pid = process_entry.get()
        if pid and rid:
            rag.assign_edge(rid, pid)
            draw_graph(rag.graph)
        else:
            messagebox.showerror("Error", "Please enter both Resource and Process IDs")

    def detect_deadlock():
        cycles = rag.detect_deadlock()
        if cycles:
            messagebox.showwarning("Deadlock Detected!", f"Deadlock cycle(s) found: {cycles}")
        else:
            messagebox.showinfo("No Deadlock", "No deadlock detected.")
        draw_graph(rag.graph, cycles)

    def resolve_all_deadlocks():
        cycles = rag.detect_deadlock()
        if cycles:
            removed_edges = []
            for cycle in cycles:
                if len(cycle) > 1:
                    u, v = cycle[0], cycle[1]
                    if rag.graph.has_edge(u, v):
                        rag.graph.remove_edge(u, v)
                        removed_edges.append((u, v))
            if removed_edges:
                msg = "Resolved deadlock by removing edges:\n"
                msg += "\n".join([f"{u} -> {v}" for u, v in removed_edges])
                messagebox.showinfo("Deadlock Resolved", msg)
            else:
                messagebox.showinfo("Info", "Deadlocks detected but no removable edges found.")
            draw_graph(rag.graph)
        else:
            messagebox.showinfo("No Deadlock", "No deadlock detected.")

    # Button Frame
    button_frame = tk.Frame(root, bg="#000000")
    button_frame.pack(pady=20)

    def styled_button(text, command):
        return tk.Button(
            button_frame, text=text, command=command, 
            width=25, bg=button_bg, fg=button_fg, font=font_family,
            activebackground="#e0e0e0", activeforeground="#000000", bd=0, pady=6
        )

    # Adding all buttons
    styled_button("Add Process", add_process).pack(pady=5)
    styled_button("Add Resource", add_resource).pack(pady=5)
    styled_button("Request Resource", request_resource).pack(pady=5)
    styled_button("Assign Resource", assign_resource).pack(pady=5)
    styled_button("Detect Deadlock", detect_deadlock).pack(pady=5)
    styled_button("Resolve All Deadlocks", resolve_all_deadlocks).pack(pady=5)

    root.mainloop()
