import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

class GraphApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Graph App")
        self.master.geometry("1000x800")

        self.functions = []
        self.axes_limits = [(0, 100), (0, 100)]

        self.create_widgets()

    def create_widgets(self):
        # Frame for input and buttons
        input_frame = tk.Frame(self.master)
        input_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Coefficient input
        tk.Label(input_frame, text="Coefficient:").grid(row=0, column=0, padx=10, pady=10)
        self.coeff_entry = tk.Entry(input_frame, width=5)
        self.coeff_entry.grid(row=0, column=1, padx=10, pady=10)

        # Function selection
        tk.Label(input_frame, text="Function:").grid(row=0, column=2, padx=10, pady=10)
        self.function_var = tk.StringVar(input_frame)
        self.function_var.set("linear")
        self.function_options = ["linear", "logarithmic", "square", "root", "sin", "cos", "tan", "ctg"]
        self.function_menu = tk.OptionMenu(input_frame, self.function_var, *self.function_options)
        self.function_menu.grid(row=0, column=3, padx=10, pady=10)

        # Constant input
        tk.Label(input_frame, text="Constant:").grid(row=0, column=4, padx=10, pady=10)
        self.const_entry = tk.Entry(input_frame, width=5)
        self.const_entry.grid(row=0, column=5, padx=10, pady=10)

        # Axis limits input
        tk.Label(input_frame, text="X-axis min:").grid(row=2, column=0, padx=10, pady=10)
        self.x_min_entry = tk.Entry(input_frame, width=5)
        self.x_min_entry.grid(row=2, column=1, padx=10, pady=10)
        tk.Label(input_frame, text="X-axis max:").grid(row=2, column=2, padx=10, pady=10)
        self.x_max_entry = tk.Entry(input_frame, width=5)
        self.x_max_entry.grid(row=2, column=3, padx=10, pady=10)
        tk.Label(input_frame, text="Y-axis min:").grid(row=3, column=0, padx=10, pady=10)
        self.y_min_entry = tk.Entry(input_frame, width=5)
        self.y_min_entry.grid(row=3, column=1, padx=10, pady=10)
        tk.Label(input_frame, text="Y-axis max:").grid(row=3, column=2, padx=10, pady=10)
        self.y_max_entry = tk.Entry(input_frame, width=5)
        self.y_max_entry.grid(row=3, column=3, padx=10, pady=10)

        # Set axis limits button
        set_button = tk.Button(input_frame, text="Set", command=self.set_axis_limits)
        set_button.grid(row=3, column=4, padx=10, pady=10)

        # Graph
        self.fig = plt.Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlim(0, 100)
        self.ax.set_ylim(0, 100)
        self.ax.set_xlabel("X-axis")
        self.ax.set_ylabel("Y-axis")
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Add function to plot
        def add_function():
            coeff = float(self.coeff_entry.get())
            const = float(self.const_entry.get())
            function_label = self.function_var.get()
            x = np.linspace(0, 100, 100)
            if function_label == "linear":
                y = coeff * x + const
            elif function_label == "logarithmic":
                y = coeff * np.log(x) + const
            elif function_label == "root":
                y = coeff * np.sqrt(x) + const
            elif function_label == "square":
                y = coeff * x**2 + const
            elif function_label == "sin":
                y = coeff * np.sin(x) + const
            elif function_label == "cos":
                y = coeff * np.cos(x) + const
            self.ax.plot(x, y, label=function_label)
            self.ax.legend()
            self.canvas.draw()

        self.add_function_button = tk.Button(input_frame, text="Draw", command=add_function)
        self.add_function_button.grid(row=4, column=0, padx=10, pady=10)

        # Clear graph button
        clear_button = tk.Button(input_frame, text="Clear", command=self.clear_graph)
        clear_button.grid(row=4, column=1, padx=10, pady=10)


    def set_axis_limits(self):
        x_min = float(self.x_min_entry.get())
        x_max = float(self.x_max_entry.get())
        y_min = float(self.y_min_entry.get())
        y_max = float(self.y_max_entry.get())
        self.axes_limits = [(x_min, x_max), (y_min, y_max)]
        self.ax.set_xlim(x_min, x_max)
        self.ax.set_ylim(y_min, y_max)
        self.canvas.draw()

    def clear_graph(self):
        self.ax.clear()
        self.ax.set_xlabel("X-axis")
        self.ax.set_ylabel("Y-axis")
        self.canvas.draw()

    def add_and_draw_function(self):
        self.add_function()
        self.clear_graph()
        self.set_axis_limits()
        for function in self.functions:
            self.ax.plot(np.linspace(0, 100, 100), eval(function), label=function)
        self.ax.legend()
        self.canvas.draw()

def main():
    root = tk.Tk()
    app = GraphApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
