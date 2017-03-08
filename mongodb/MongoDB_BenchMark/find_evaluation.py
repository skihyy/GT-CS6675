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
    with open('find.csv', 'w') as wf:
        writer = csv.writer(wf)
        writer.writerow(['time', '1sec', 'total'])
        cur_time = time.time()
        total = 0
        this_period_writen = 0
        id = 0
        spent_time = 0
        print('Start to insert.')
        for row in reader:
            search_condition = {'id': str(id), 'field0': str(row[10])}
            id += 1
            # find
            print('Find: ' + str(id))
            collection.find(search_condition)
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
