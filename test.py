import tkinter as tk
import matplotlib

matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Matplotlib Demo')

        data = {
            'Python': 10,
            'C': 11,
            'Java': 15,
            'C++': 7,
            'C#': 9
        }

        languages = data.keys()
        popularity = data.values()

        figure = Figure(figsize=(6, 4), dpi=100)
        figure_canvas = FigureCanvasTkAgg(figure, self)
        NavigationToolbar2Tk(figure_canvas, self)
        axes = figure.add_subplot()

        axes.bar(languages, popularity)
        axes.set_title('Top 5 languages')
        axes.set_ylabel('Popularity')

        figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


if __name__ == '__main__':
    app = App()
    app.mainloop()



