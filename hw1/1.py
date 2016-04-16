import os
import json
import math
user_records = []
tmp_file_name = 'tmp_user_records'
new_tmp_file = 'new_tmp_file'
if os.path.exists(tmp_file_name):
    with open(tmp_file_name) as f:
        for line in f:
            try:
                json_line = json.loads(line)
                if (not (math.isnan(json_line['lon']))) and (not (math.isnan(json_line['lat']))):
                	user_records.append(json_line)
            except:
                continue

processed_users = set()
for r in user_records:
    try:
        processed_users.add(r['uid'])
    except:
        print r

print len(processed_users)
i = 0
new_f = open(new_tmp_file, 'w')
for usr in processed_users:
	for rec in user_records:
		if rec['uid'] == usr:
			json.dump(rec, new_f)
			new_f.write('\n')
			i += 1
			break

new_f.close()
print i
