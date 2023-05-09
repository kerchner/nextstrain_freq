# README: 
# Get help from Daniel Kerchner at GW lib. 
# This file needs to be run to update frequency data from Nextstrain.org
# Have to activate the environment (ENV)
# Run the two lines below in terminal:
  # source ENV/bin/activate
  # python3 convert.py

# NOTE: I also have to download the nextstrain_ncov_open_global_all-time_metadata from Nextstrain.org also.

import requests
import json
import csv
# import pandas as pd

outfile = open("Nextstrain_opensource_frequenices.csv", "w")
writer = csv.writer(outfile)
writer.writerow(["strain", "week", "frequency"])

url = requests.get("https://nextstrain.org/charon/getDataset?prefix=ncov/open/global/all-time&type=tip-frequencies")
data = json.loads(url.text)

# df = pd.DataFrame(columns = ['strain', 'week', 'frequency'])

del data['generated_by'] # delete 'generated_by'
pivots = data.pop('pivots') # remove 'pivots' from data but store it

for strain, freq_dict in data.items():
    freq_list = freq_dict['frequencies']
    for week_num in range(0, len(freq_list)):
        freq = freq_list[week_num]
   #    df = df.append({'strain': strain, 'week': week_num, 'frequency': freq}, ignore_index=True)
        writer.writerow([strain, week_num, freq])
outfile.close()

pivotfile = open("Nextstrain_opensource_pivotdates.csv", "w")
pivot_writer = csv.writer(pivotfile)
for pivot in pivots: 
    pivot_writer.writerow([pivot])
pivotfile.close()
