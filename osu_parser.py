from tkinter import filedialog
import tkinter as tk

from cv2 import phase


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
    if phrase == '[Colours]':
        get_line('[HitObjects]')

general_line = get_line('[General]')
editor_line = get_line('[Editor]')
metadata_line = get_line('[Metadata]')
difficulty_line = get_line('[Difficulty]')
events_line = get_line('[Events]')
timing_line = get_line('[TimingPoints]')
Colours_line = get_line('[Colours]')
hit_line = get_line('[HitObjects]')


# Get datas of each section
general_list = osu_data[general_line:editor_line-1]
editor_list = osu_data[editor_line:metadata_line-1]
metadata_list = osu_data[metadata_line:difficulty_line-1]
difficulty_list = osu_data[difficulty_line:events_line-1]
events_list = osu_data[events_line:timing_line-1]
timingpoints_list = osu_data[timing_line:Colours_line-1]
Colours_list = osu_data[Colours_line:hit_line-1]
hitobject_list = osu_data[hit_line:]