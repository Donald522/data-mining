import os
import json
import math

i = 0
new_tmp_file = 'tmp_user_records'
if os.path.exists(new_tmp_file):
	with open(new_tmp_file) as new_f:
		for l in new_f:
			try:
				line = json.loads(l)
				if (not (math.isnan(line['lon']))) and (not (math.isnan(line['lat']))):
					i += 1
			except:
				continue
print i
