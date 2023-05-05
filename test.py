import tkinter
import tkinter.scrolledtext as st

class App(tkinter.Tk):
    def __init__(self):
        super().__init__()

        self.protocol("WM_DELETE_WINDOW", self.destroy)
        self.bind('<Escape>', lambda e: self.destroy())

        menubar = tkinter.Menu(self)
        filemenu = tkinter.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", command=self.destroy)
        menubar.add_cascade(label="File", menu=filemenu)
        self.config(menu=menubar)

        txt = st.ScrolledText(self, undo=True)
        txt['font'] = ('Times New Roman', '14')
        txt.pack(expand=True, fill='both')


if __name__ == '__main__':
    app = App()
    app.mainloop()

