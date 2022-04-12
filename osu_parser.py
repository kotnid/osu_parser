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
    if phrase == '[colours]':
        return get_line('[hitObjects]') -1

general_line = get_line('[general]')
editor_line = get_line('[editor]')
metadata_line = get_line('[metadata]')
difficulty_line = get_line('[difficulty]')
events_line = get_line('[events]')
timing_line = get_line('[timingPoints]')
Colours_line = get_line('[colours]')
hit_line = get_line('[hitObjects]')


# Get datas of each section
general_list = osu_data[general_line:editor_line-1]
editor_list = osu_data[editor_line:metadata_line-1]
metadata_list = osu_data[metadata_line:difficulty_line-1]
difficulty_list = osu_data[difficulty_line:events_line-1]
events_list = osu_data[events_line:timing_line-1]
timingpoints_list = osu_data[timing_line:Colours_line-1]
colours_list = osu_data[Colours_line:hit_line-1]
hitobject_list = osu_data[hit_line:]


# Transfer datas of section which content type is pairs
pairs_sections = [general_list , editor_list , metadata_list , difficulty_list , colours_list]
pairs_name = ['general' , 'editor' , 'metadata' , 'difficulty' , 'colours' ]

for i in range(len(pairs_sections)):
    for item in pairs_sections[i]:
        if ':' in item:
            item = item.split(': ')
            data[pairs_name[i]][item[0]] = item[1]