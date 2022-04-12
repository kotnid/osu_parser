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
data['general'] = {}
data['editor'] = {}
data['metadata'] = {}
data['difficulty'] = {}
data['events'] = []
data['timingpoints'] = []
data['colours'] = {}
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


# Transfer datas of Timing points
for item in timingpoints_list:
    if ',' in item:
        item = item.split(',')
        point = {
        'time':item[0],
        'beatLength':item[1],
        'meter':item[2],
        'sampleSet':item[3],
        'sampleIndex':item[4],
        'volume':item[5],
        'uninherited':item[6],
        'effects':item[7]
        }
       
        data['timingpoints'].append(point)


# Transfer datas of Events
for item in events_list:
    item = item.split(',')
    point = {
        'eventType':item[0],
        'startTime':item[1],
    }

    if item[0] == '0':
        point['filename'] = item[2]
        point['xoffset'] = item[3]
        point['yoffset'] = item[4]
        data['events'].append(point)
    
    elif item[0] == '1' or item[0] == 'Video':
        point['filename'] = item[2]
        point['xoffset'] = item[3]
        point['yoffset'] = item[4]
        data['events'].append(point)

    elif item[0] == '2' or item[0] == 'Break':
        point['endTime'] = item[2]
        data['events'].append(point)
