import csv
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'data'/'safety_run_chart_synthetic.csv'
with p.open(newline='',encoding='utf-8') as f: rows=list(csv.DictReader(f))
for r in rows:
 rate=1000*float(r['restraint_events'])/float(r['patient_days'])
 print(f"Fictional month {r['month']:>2}: {rate:.2f} events / 1,000 patient-days")
print('SYNTHETIC DATA. Not facility incident reports. Not evidence of the career-reported 80% reduction.')
