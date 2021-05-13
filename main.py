import install as install
import pandas as pd
import numpy as num
import matplotlib as ml

from tkinter import*
from PIL import ImageTk

class Login:
    def __init__(self, root):
        self.root=root
        self.root.title("Traffic Management System")
        self.root.geometry("1000x600+400+200")

        self.root.configure(background="#202020")

        name = Entry(root, text=("Enter Name")).grid(row=2, column=0)

root = Tk()
obj=Login(root)
root.mainloop()