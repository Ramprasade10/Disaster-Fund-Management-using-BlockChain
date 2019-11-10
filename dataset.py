import random,csv
res = [] 
# afile = open("dataset.csv", "w" )
num=10000
csvfile=open('dataset.csv','wb')
obj=csv.writer(csvfile)
for j in range(num):
        line=random.randint(1000,5000),random.randint(1,4),random.choice([100,101,102]),random.randint(4,10)
        # afile.write(str(line))
        print(str(line))
        obj.writerow(line)
csvfile.close()
# afile.close()