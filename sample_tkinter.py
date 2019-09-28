import mychart

# file open関係
import os
import tkinter as tk
import tkinter.filedialog, tkinter.messagebox

class SampleApp(tk.Frame) :
    def __init__(self, master=None):
        super().__init__(master)
        self.master.geometry()
        self.master.title("テスト")

        self.menu_bar = tk.Menu(self.master)
        self.master.config(menu=self.menu_bar)

        self.create_widgets()

    def create_widgets(self):
        file_menu = tk.Menu(self.menu_bar)
        file_menu.add_command(label="Close", command=self.master.quit)
        self.menu_bar.add_cascade(label="Menu", menu=file_menu)

        self.label = tk.Label(self.master, text="asdf")
        self.label.grid(row=1, column=1)

        self.edit = tk.Entry(self.master, width=100)
        self.edit.grid(row=1, column=1)

        self.button = tk.Button(self.master, text="Open", command=lambda : self.openLogFile())
        self.button.grid(row=1,column=2)

        self.button2 = tk.Button(self.master, text="Show Chart", command=lambda : mychart.showChart(file_name=self.fname))
        #button2 = tk.Button(frame, text="Show Chart", command=lambda : filenameCheck())
        self.button2.grid(row=2,column=1,columnspan=2)

    def openLogFile(self) :
        # ダイアログの表示
        ftyp = [("csv files", "*.csv")]
        idir = os.path.abspath(os.path.dirname(__file__))
        self.fname = tk.filedialog.askopenfilename(filetypes = ftyp, initialdir = idir)
        self.edit.delete(0, tk.END)
        self.edit.insert(0, self.fname)

    def filenameCheck(self) :
        tk.messagebox.showinfo("check", self.fname)

root = tk.Tk()
app = SampleApp(master=root)
app.mainloop()
