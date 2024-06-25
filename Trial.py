import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

root = ctk.CTk()
root.title("Data Visualisation")
root.geometry("1200x800")

tab_view = ctk.CTkTabview(root)
tab_view.pack(fill="both", expand=True)

tab_view.add("Accumulator")
tab_view.add("Motor")
tab_view.add("Temp")

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.sinh(x)
y5 = np.cosh(x)
y6 = np.tanh(x)

y_values = [y1, y2, y3, y4, y5, y6]
titles = ["Graph 1", "Graph 2", "Graph 3", "Graph 4", "Graph 5", "Graph 6"]

def create_graphs(tab, x, y_values, titles):
    for i, (y, title) in enumerate(zip(y_values, titles)):
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_title(title)
        fig.patch.set_alpha(0.0)
        ax.patch.set_alpha(0.0)

        canvas = FigureCanvasTkAgg(fig, master=tab)
        canvas.draw()
        row = i // 3
        col = i % 3
        canvas.get_tk_widget().grid(row=row, column=col, padx=10, pady=10, sticky='nsew')

for tab_name in ["Accumulator", "Motor", "Temp"]:
    tab = tab_view.tab(tab_name)
    tab.grid_rowconfigure((0, 1), weight=1)
    tab.grid_columnconfigure((0, 1, 2), weight=1)
    create_graphs(tab, x, y_values, titles)

root.mainloop()
