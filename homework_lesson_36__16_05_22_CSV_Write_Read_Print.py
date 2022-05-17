### Task 1 ###

import csv
homework_data = [['hostname', 'vendor', 'model', 'location'],
                 ['sw1', 'Cisco', '3750', 'London'],
                 ['sw2', 'Cisco', '3850', 'Liverpool'],
                 ['sw3', 'Cisco', '3650', 'Liverpool'],
                 ['sw4', 'Cisco', '3650', 'London']]
with open('homework_36.csv', 'w') as fhw:
    writer = csv.writer(fhw, delimiter=';', lineterminator='\r', quoting=csv.QUOTE_NONNUMERIC)
    for row in homework_data:
        writer.writerow(row)

with open('homework_36.csv') as fhw:
    print(fhw.read())
