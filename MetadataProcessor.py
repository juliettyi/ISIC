import csv
import json
import os

def MaybeAdd(l, d, k):
  '''Add d[k] to end of l, if k is in d.'''
  if k in d:
    l.append(d[k])
  else:
    l.append('')

file_list = os.listdir('Descriptions/')
idx = 0

# output for further ananlysis.
ofn = 'meta.csv'
of = csv.writer(open(ofn, 'w'))

header = [
  'id',
  'age',
  'diag_confirm',
  'anatom_site',
  'sex',
  'diag',
  'benign',
  'melanocytic',
  'y',
  'x',
  'image_type'
]
of.writerow(header)

# each file is the meta data for one image.
for fn in file_list:
  with open(os.path.join('Descriptions/', fn)) as f:
    meta = json.loads(f.read())
    if not 'meta' in meta:
      print('%s missing meta' % fn)
      continue
    data = [fn]
    if 'clinical' in meta['meta']:
      c = meta['meta']['clinical']
      MaybeAdd(data, c, 'age_approx')
      MaybeAdd(data, c, 'diagnosis_confirm_type')
      MaybeAdd(data, c, 'anatom_site_general')
      MaybeAdd(data, c, 'sex')
      MaybeAdd(data, c, 'diagnosis')
      MaybeAdd(data, c, 'benign_malignant')
      MaybeAdd(data, c, 'melanocytic')

    if 'acquisition' in meta['meta']:
      a = meta['meta']['acquisition']
      MaybeAdd(data, a, 'pixelsY')
      MaybeAdd(data, a, 'pixelsX')
      MaybeAdd(data, a, 'image_type')

    of.writerow(data)
