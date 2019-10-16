
import csv
from operator import itemgetter

INDUSTRIES = ['Agriculture', 'Business services', 'Construction', 'Leisure/hospitality', 'Manufacturing']

def read_file(fp):
    '''Docstring'''
    reader = csv.reader(fp)
    next(reader,None)
    next(reader,None)
    next(reader,None)
    list1 = []
    for line in reader:
        if not line[0]: # gets rid of line with no data 
            continue # goes through the line 
        list1.append(line)
    return list1[:-6]

def get_totals(L):
    '''Docstring'''
    us = 0
    total = 0

    for line in L:
        if line[0] == "U.S.":
            us = int(line[1].replace(",", ""))
        else:
            if '<' in line[1]:
                line[1] = line[1].replace("<", "")
            total += int(line[1].replace(",", ""))
                
    return us,total  # temoprary return value so main runs

def get_industry_counts(L):
    '''Docstring'''
    L2 = []  
    l = [0,0,0,0,0]
    for line in L: 
        if line[0] == "U.S.":
            continue
        if line[9] == 'Construction':
            l[2] += 1 
        elif line[9] == 'Manufacturing':
            l[4] += 1
        elif line[9] == 'Leisure/hospitality':
            l[3] += 1
        elif line[9] == 'Business services':
            l[1] += 1
        elif line[9] == 'Agriculture':
            l[0] += 1     
    for i in range(5):
        L2.append([INDUSTRIES[i], l[i]])
    L2 = sorted(operator.itemgetter(1))
    return L2

def get_largest_states(L):
    '''Docstring'''
    L2 = []
    for line in L:
        num = float(line[2].replace("%", ""))
        if num > 3.3:
            L2.append(line[0])
    return L2  # temoprary return value so main runs

def main():    
    fp = open("immigration.csv")
    L = read_file(fp)
    print(L)
    
    us_pop,total_pop = get_totals(L)
    if us_pop and total_pop:  # if their values are not None
        print("\nData on Illegal Immigration\n")
        print("Summative:", us_pop)
        print("Total    :", total_pop)
    
    states = get_largest_states(L)
    if states:  # if their value is not None
        print("\nStates with large immigrant populations")
        for state in states:
            state = state.replace('\n',' ')
            print(state)        
    
    counters = get_industry_counts(L)
    if counters:  # if their value is not None
        print("\nIndustries with largest immigrant populations by state")
        print("{:24s} {:10s}".format("industry","count"))
        for tup in counters:
            print("{:24s} {:2d}".format(tup[0],tup[1]))
        
if __name__ == "__main__":
    main()