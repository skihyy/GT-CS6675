import time
import csv
from pymongo import MongoClient

client = MongoClient('127.0.0.1', 27017)
# database
db = client['test_database']
# collection
collection = db['test_collection']

with open('sample.csv', 'r') as rf:
    reader = csv.reader(rf)
    with open('save.csv', 'w') as wf:
        writer = csv.writer(wf)
        writer.writerow(['time', '1sec', 'total'])
        cur_time = time.time()
        total = 0
        this_period_writen = 0
        id = 0
        spent_time = 0
        print('Start to insert.')
        for row in reader:
            data = {'id': str(id), 'field0': str(row[10]), 'field1': str(row[11]), 'field2': str(row[12]),
                    'field3': str(row[13]), 'field4': str(row[14]), 'field5': str(row[5]), 'field6': str(row[6]),
                    'field7': str(row[7]), 'field8': str(row[8]), 'field9': str(row[9]), 'field10': str(row[10]),
                    'field11': str(row[1]), 'field12': str(row[2]), 'field13': str(row[3]), 'field14': str(row[4])}
            id += 1
            # save
            print('Save: ' + str(id))
            collection.save(data)
            this_period_writen += 1
            # 1 sec
            if 1 <= time.time() - cur_time:
                total += this_period_writen
                writer.writerow([spent_time, this_period_writen, total])
                this_period_writen = 0
                spent_time += 1
                cur_time = time.time()
    wf.close()
rf.close()
