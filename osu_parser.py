from tkinter import filedialog
import tkinter as tk

root = tk.Tk()
root.withdraw()
osu_file = filedialog.askopenfilename()
osu_data = open(osu_file,'r+').readlines()