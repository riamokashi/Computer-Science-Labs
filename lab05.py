file=open("data.txt",'r')
file.readline()
lst=[]
for line in file:
    line=line.strip().split(" ")
    lst.append(line)

total_height=0
total_weight=0
count=0

bmi_lst=[]
for i in range(len(lst)):
    h=float(lst[i][1])
    w=float(lst[i][2])
    bmi=w/(h*h)
    bmi_lst.append(bmi)

max_height=0
max_weight=0
min_height=100000
min_weight=100000
max_bmi=0
min_bmi=100000

for i in range(len(bmi_lst)):
    if max_bmi < bmi_lst[i]:
        max_bmi = bmi_lst[i]
    if min_bmi > bmi_lst[i]:
        min_bmi=bmi_lst[i]
  
for i in range(len(lst)):
    count+=1
    total_height+=float(lst[i][1])
    if max_height< float(lst[i][1]):
        max_height=float(lst[i][1])
    if min_height> float(lst[i][1]):
        min_height=float(lst[i][1])
        total_weight+=float(lst[i][2])
  
    if max_weight< float(lst[i][2]):
        max_weight=float(lst[i][2])
    if min_weight> float(lst[i][2]):
        min_weight=float(lst[i][2])
    
avg_height=total_height/count
avg_weight=total_weight/count
avg_bmi=sum(bmi_lst)/len(bmi_lst)

#printing
print("{:<12s}{:<12s}{:<12s}{:<12s}".format("Name","Height(m)","Weight(kg)","BMI"))
for i in range(len(lst)):
    print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format(lst[i][0],float(lst[i][1]),float(lst[i][2]),bmi_lst[i]))
print()
print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Average",avg_height,avg_weight,avg_bmi))
print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Max",max_height,max_weight,max_bmi))
print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Min",min_height,min_weight,min_bmi))

outfile=open("output.txt",'w')
#printing to file
print("{:<12s}{:<12s}{:<12s}{:<12s}".format("Name","Height(m)","Weight(kg)","BMI"),file=outfile)
for i in range(len(lst)):
    print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format(lst[i][0],float(lst[i][1]),float(lst[i][2]),bmi_lst[i]),file=outfile)
print(" ",file=outfile)
print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Average",avg_height,avg_weight,avg_bmi),file=outfile)
print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Max",max_height,max_weight,max_bmi),file=outfile)
print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Min",min_height,min_weight,min_bmi),file=outfile)
outfile.close()