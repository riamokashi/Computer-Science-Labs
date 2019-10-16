def open_file(file):
    return open('scores.txt')

def read_file(file_name):
    records = []
    for l in file_name:
        records.append(l.strip().split())
    records.sort()
    
    ex1 = 0
    ex2 = 0
    ex3 = 0 
    ex4 = 0
    print("{:20s}{:6s}{:6s}{:6s}{:6s}{:>10s}".format("Name", "Exam1", "Exam2", "Exam3", "Exam4", "Mean"))

    for line in records:
        records = [int(x) for x in line[2:]]
        name = " ".join(line[:2])
        mean = sum(records)/4
        mean = round(mean, 2)
        print('{:21s}{:6d}{:6d}{:6d}{:6d}{:^12f}'.format(name, records[0], records[1], records[2], records[3], mean))
        ex1 += records[0]
        ex2 += records[1]
        ex3 += records[2]
        ex4 += records[3]
    print("{:20s}{:6d}{:6d}{:6d}{:6d}{:10.2f}".format("Exam Mean ", ex1/5, int(ex2/5), int(ex3/5),int(ex4/5), mean))

fp = open_file('scores.txt')  
read_file(fp) 
    
#    
#        print('{:21s}{:6s}{:6s}{:6s}{:6s}{:^12s}'.format('Name', 'Exam1', 'Exam2', 'Exam3', 'Exam4', 'Mean'))
#
#            print('{:20s}{:6d}{:6d}{:6d}{:6d}{:10.2f}'.format(record[0], record[1], record[2], record[3], record[4], mean))
#
#    print('{:20s}{:6.1f}{:6.1f}{:6.1f}{:6.1f}'.format('Exam Mean',exam_one/sz,exam_two/sz, 
#
#    
#    
    