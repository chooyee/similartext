from pprint import pp
import json
 
# Opening JSON file
f = open('uat-industry.json')

data = json.load(f)
 
with open("industry_clean.txt", "w") as fp:
    for i in data:
        pp(i['label'])
        fp.write(i['label'].strip() + "\n")
 
# Closing file
f.close()