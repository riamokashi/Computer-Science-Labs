#PART A
open_file=open('data.txt')

count=0
min_height=10000
max_height=0
sum_height=0
min_weight=10000
max_weight=0
sum_weight=0
min_bmi=10000
max_bmi=0
sum_bmi=0
for line in open_file:
    line=line.strip()
    elements_data=line.split()
    name=elements_data[0]

    if count>0:
        height=float(elements_data[1])
        weight=float(elements_data[2])
        bmi=weight/height**2
        if bmi<min_bmi:
            min_bmi=bmi
        if bmi>max_bmi:
            max_bmi=bmi
        sum_bmi+=bmi
        avg_bmi=sum_bmi/8

        if height<min_height:
            min_height=height
        if height>max_height:
            max_height=height
        sum_height+=height
        avg_height=sum_height/8
        if weight<min_weight:
            min_weight=weight
        if weight>max_weight:
            max_weight=weight
        sum_weight+=weight
        avg_weight=sum_weight/8
        print (line,'{:10.2f}'.format(bmi))
    else:
        count+=1
        print (line,'BMI')
print('{:s}{:9.2f}{:13.2f}{:11.2f}{:s}{:13.2f}{:13.2f}{:11.2f}{:s}{:13.2f}{:13.2f}{:11.2f}'.format('\nAverage',avg_height,avg_weight,avg_bmi,'\nMax',max_height,max_weight,max_bmi,'\nMin',min_height,min_weight,min_bmi))
open_file.close()

#PART B
infile=open('data.txt')
outfile = open("output.txt","w")
counter=0
heightMin=10000
weightMin=10000
bmiMin=10000
heightMax=0
weightMax=0
bmiMax=0
sum_height=0
sum_weight=0
sum_bmi=0
for line in infile:
    line=line.strip()
    dataItems=line.split()
    name=dataItems[0]
    if counter>0:
        height=float(dataItems[1])
        h =height
        weight=float(dataItems[2])
        w=weight
        bmi=weight/height**2
      
        if bmi<bmiMin:
            bmiMin=bmi
        if bmi>bmiMax:
            bmiMax=bmi
        sum_bmi+=bmi
        avg_bmi=sum_bmi/8

        if height<heightMin:
            heightMin=height
        if height>heightMax:
            heightMax=height
        sum_height+=height
        avg_height=sum_height/8

        if weight<weightMin:
            weightMin=weight
        if weight>weightMax:
            weightMax=weight
        sum_weight+=weight
        avg_weight=sum_weight/8
        print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format(name,h,w,bmi),file=outfile)
    else:
        counter+=1
        print("{:<12s}{:<12s}{:<12s}{:<12s}".format("Name","Height(m)","Weight(kg)","BMI"),file=outfile)
print(file=outfile)
print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Average",avg_height,avg_weight,avg_bmi),file=outfile)
print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Max",heightMax,weightMax,bmiMax),file=outfile)
print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Min",heightMin,weightMin,bmiMin),file=outfile)
infile.close()
outfile.close()