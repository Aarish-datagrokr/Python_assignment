import re
import pprint
import json
import sys
from json import JSONEncoder


class setEncoder(JSONEncoder):
    def default(self, obj):
        return list(obj)


name = sys.argv[1]
query = ''
json_obj = []
with open(name, 'r') as sql_file:
    query = sql_file.read()

    sql_statements = query.split(';')
    count = 1
    final_output = []
    for statement in sql_statements:
        mp = {}
        mp['statement_id'] = count
        keywords = re.split('\n| |,', statement.strip())
        s = set()
        se = set()
        mp['target_table_name'] = []
        if keywords[0] == 'INSERT' or 'UPDATE' or 'CREATE':
            mp['statement_type'] = keywords[0].lower()
        for idx, val in enumerate(keywords):
            if val == 'FROM' or val == 'JOIN':
                se.add(val)
                s.add(keywords[idx + 1])

        mp2 = {}
        mp2['type'] = se
        mp2['name'] = s
        mp['target_table_name'].append(mp2)
        count += 1
        json_obj.append(mp)

with open("sample_stored_procedure.json", "w") as outfile:
    pprint.pprint(json_obj)
    json.dump(json_obj, outfile, indent=4, cls=setEncoder)

