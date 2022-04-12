from tkinter import filedialog
import tkinter as tk

# Get file to parse
root = tk.Tk()
root.withdraw()
osu_file = filedialog.askopenfilename()
osu_data = open(osu_file,'r+').readlines()

# Init place for data to store
data = {}
data['General'] = {}
data['Editor'] = {}
data['Metadata'] = {}
data['Difficulty'] = {}
data['Events'] = []
data['timingpoints'] = []
data['Colours'] = {}
data['hitobjects'] = []
