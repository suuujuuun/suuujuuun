import tkinter as tk
from tkinter import messagebox
from parser import parse_logic
from graph.builder import build_graph
from graph.visualizer import visualize_graph

def launch_input_window():
    def on_submit():
        user_input = text_box.get("1.0", tk.END).strip()
        if not user_input:
            messagebox.showerror("Error", "Input cannot be empty")
            return

        try:
            parsed = parse_logic(user_input)
            graph = build_graph(parsed)
            visualize_graph(graph)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    root = tk.Tk()
    root.title("Logic Visualizer")

    label = tk.Label(root, text="Enter logical expressions (e.g., IF A AND B THEN C OR D):")
    label.pack(pady=10)

    format_info = tk.Label(
        root,
        text=(
            "Supported format:\n"
            "- IF A THEN B\n"
            "- IF A AND B THEN C\n"
            "- IF A THEN B AND C\n"
            "- IF A AND B THEN C AND D\n"
            "- IF A OR B THEN C\n"
            "- IF A THEN B OR C\n"
            "- Parentheses supported: IF (A AND B) OR C THEN (D AND E)\n"
            "- Multiple lines allowed\n"
            "(Each line must follow the 'IF ... THEN ...' structure)"
        ),
        justify="left",
        fg="gray",
    )
    format_info.pack(pady=5)

    text_box = tk.Text(root, height=10, width=60 , font=("Helvetica", 20))
    text_box.pack(pady=5)

    button = tk.Button(root, text="Visualize", command=on_submit)
    button.pack(pady=20)

    root.mainloop()
