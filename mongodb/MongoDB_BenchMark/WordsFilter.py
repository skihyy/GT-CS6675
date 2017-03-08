import csv
with open('sample.csv', 'w') as wf:
    writer = csv.writer(wf)
    with open('enwiki-20170120-pages-articles-multistream-index.txt', 'r') as rf:
        lines = 0
        ct = 0;
        row = []
        for line in rf:
            words = line.split(":")
            for word in words:
                if 0 < len(word):
                    final_words = word.split(" ")
                    for fw in final_words:
                        if 0 < len(fw):
                            w = str(fw).strip()
                            row.append(w)
                            ct += 1;
                            if 15 == ct:
                                writer.writerow(row)
                                ct = 0
                                row = []
                                lines += 1
        print('lines: ' + str(lines))
    rf.close()
wf.close()