import csv, statistics
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'data'/'a3_encounters_synthetic.csv'
with p.open(newline='',encoding='utf-8') as f: r=list(csv.DictReader(f))
waits=[int(x['wait_minutes']) for x in r]
print('SYNTHETIC ambulatory wait-time example')
print('Encounters:',len(r),'Mean wait:',round(statistics.mean(waits),1),'minutes')
print('Median:',statistics.median(waits),'| >60 min:',sum(w>60 for w in waits),'| within 15 min:',sum(w<=15 for w in waits))
print('No real clinic patients, no implemented improvement outcomes.')
