import numpy as np
import pandas as pd

missing_schools = [
    'HOYNE',
    'MELODY',
    'BROWNELL',
    'MCAULIFFE',
    'DECATUR',
    'KIPP CHICAGO - ASCEND PRIMARY',
    'JORDAN',
    'LELAND',
    'VOISE HS',
    'CASALS',
    'BRONZEVILLE HS',
    'LORCA',
    'BLACK',
    'CHRISTOPHER',
    'POE'
]

fusion = pd.read_csv('cps_fusion_table.raw.csv')

d = []

for school in missing_schools:
    lat_long = fusion[fusion.SchoolName == school][['Lat', 'Long']].values[0]
    d.append((school.title(), np.nan, np.nan, lat_long[0], lat_long[1]))

null_schools = pd.DataFrame(d, columns=['schoolname', 'score', 'num_fixtures', 'lat', 'long'])

out = pd.read_csv('lead_scores.csv')
out = out.append(null_schools).reset_index(drop=True)
out.to_csv('lead_scores.csv', index=False)
