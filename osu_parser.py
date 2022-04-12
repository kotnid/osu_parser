from tkinter import filedialog
import tkinter as tk

# Get file to parse
root = tk.Tk()
root.withdraw()
osu_file = filedialog.askopenfilename()
osu_data = open(osu_file,'r+').readlines()

# Init place for datas to store
data = {}
data['General'] = {}
data['Editor'] = {}
data['Metadata'] = {}
data['Difficulty'] = {}
data['Events'] = []
data['timingpoints'] = []
data['Colours'] = {}
data['hitobjects'] = []

# Get line of datas
def get_line(phrase):
    for num, line in enumerate(osu_data, 0):
        if phrase in line:
            return num

general_line = get_line('[General]')
editor_line = get_line('[Editor]')
metadata_line = get_line('[Metadata]')
difficulty_line = get_line('[Difficulty]')
events_line = get_line('[Events]')
timing_line = get_line('[TimingPoints]')
Colours_line = get_line('[Colours]')
hit_line = get_line('[HitObjects]')
