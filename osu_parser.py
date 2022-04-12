from tkinter import filedialog
import tkinter as tk
import json

# Get file to parse
root = tk.Tk()
root.withdraw()
osu_file = filedialog.askopenfilename(filetypes=[("osu file", "*.osu")])
osu_data = open(osu_file,'r+' , encoding="utf8" ).readlines()


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
    if phrase == '[Colours]':
        return get_line('[HitObjects]') -1

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
colours_list = osu_data[Colours_line:hit_line-1]
hitobject_list = osu_data[hit_line:]


# Transfer datas of section which content type is pairs
pairs_sections = [general_list , editor_list , metadata_list , difficulty_list , colours_list]
pairs_name = ['general' , 'editor' , 'metadata' , 'difficulty' , 'colours' ]

for i in range(len(pairs_sections)):
    for item in pairs_sections[i]:
        if ':' in item:
            item = item.rstrip("\n").split(':')
            data[pairs_name[i]][item[0]] = item[1]


# Transfer datas of Timing points
for item in timingpoints_list:
    if ',' in item:
        item = item.rstrip("\n").split(',')
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
    if ',' not in item:
        continue;

    item = item.rstrip("\n").split(',')
    point = {
        'eventType':item[0],
        'startTime':item[1],
    }

    if item[0] == '0':
        point['filename'] = item[2]
        point['xoffset'] = item[3]
        point['yoffset'] = item[4]       
    
    elif item[0] == '1' or item[0] == 'Video':
        point['filename'] = item[2]
        point['xoffset'] = item[3] if 'item[3]' in locals() else ""
        point['yoffset'] = item[4] if 'item[3]' in locals() else ""

    elif item[0] == '2' or item[0] == 'Break':
        point['endTime'] = item[2]

    data['events'].append(point)


# Transfer datas of Hit objects
for item in hitobject_list:
    if ',' not in item:
        continue;
    
    item = item.rstrip("\n").split(',')
    point = {
        'x':item[0],
        'y':item[1],
        'time':item[2],
        'type':item[3],
        'hitSound':item[4]
    }

    # slider
    if item[3] == '6' or item[3] == '2':
        content = item[5].split('|')
        point['curveType'] = content[0]
        point['curvePoints'] = content[1:]
        point['slides'] = item[6]
        point['length'] = item[7]

        point['edgeSounds'] = item[8] if 'item[8]' in locals() else ""
        point['edgeSets'] = item[9] if 'item[9]' in locals() else ""
        point['hitSample'] = item[10] if 'item[10]' in locals() else ""
        

    # hit circle
    elif item[3] == '5' or item[3] == '1':
        point['hitSample'] = item[5]

    # Spinner
    elif item[3] == '12' or item[3] == '8':
        point['endTime'] = item[5]
        point['hitSample'] = item[6]

    # osu!mania hold
    else:
        content = item[5].split(':')
        point['endTime'] = content[0]
        point['hitSample'] = content[1:]

    data['hitobjects'].append(point)


# Output data
output = json.dumps(data)
filename = filedialog.asksaveasfilename(filetypes=[('json file', '*.json') ], title='Save your .json file' , initialfile = data['metadata']['Title'].rstrip()+'.json' , initialdir='C:')

if not filename.endswith('.json'):
    filename += '.json'

with open(filename,'w' ,  encoding="utf8" ) as file:
    file.write(output)