import requests
import json
import datetime

payload = {"username": "TANISIRWIN",
           "password": "lnS14WwXnzynX31"}

get_file_url = 'https://scoresdownload.collegeboard.org/pascoredwnld/file?filename='
name = '4300_20180410_111604.csv'

get_file_list = 'https://scoresdownload.collegeboard.org/pascoredwnld/files/list'
from_date = '?fromDate=2018-04-16T00:00:00-0800'
#recordCount
#fileType Essay File/Scores File
#fileName
#deliveryDate
#assessment

d = datetime.datetime.now() - datetime.timedelta(days=7)
d = str(d.isoformat())
d = d[:19] + '-0800' #trunc milliseconds and add timezone
from_date = from_date[:10] + d
print get_file_list+from_date

file_list = []
record_count = 0

r = requests.post(get_file_list+from_date, json=payload)
if r.status_code == 200:
    print 'File List'
    for file_info in r.json()['files']:
        if file_info['fileType'] != "Essay File":
            file_list.append(file_info['fileName'])
            record_count += file_info['recordCount']
            print file_info['fileName']
    print 'File count: ' + str(len(file_list))
    print 'Total records: ' + str(record_count)
    print'---'
    for file_name in file_list:
        r = requests.post(get_file_url+file_name, json=payload)
        with requests.get(r.json()['fileUrl'], stream=True) as req:
            if req.status_code == 200:
                if file_list.index(file_name) == 0:
                    print 'First file ' + file_name + ' write all.'
                    with open('../../sat_data.csv', 'w') as fd:
                        for chunk in req.iter_lines():
                            fd.write(chunk)
                            fd.write('\n')
                else:
                    print 'File ' + str(file_list.index(file_name)+1) + '; Skip header'
                    with open('../../sat_data.csv', 'a') as fd:
                        skip_line = False
                        for chunk in req.iter_lines():
                            if skip_line == False:
                                skip_line = True
                            else:
                                fd.write(chunk)
                                fd.write('\n')
            else:
                req.raise_for_status()
else:
    r.raise_for_status()
print 'Done'

