import shutil
import gzip
import os

file = [".".join(f.split(".")[:-2]) for f in os.listdir(os.getcwd()) if os.path.isfile(f)]#extract files names without ext
extention = [".".join(f.split(".")[2:]) for f in os.listdir(os.getcwd()) if os.path.isfile(f)]

num=0
for i in range (len(file)):

    if extention[i]=='gz':
        num = num + 1
        #if file[i]==''
        with gzip.open(file[i] + ".csv.gz", "rb") as f_in: #select all file with ext .gz

            with open(file[i] + ".csv", "wb") as f_out:#select files inside .gz here exemple .csv

                shutil.copyfileobj(f_in, f_out) #extraction of content .csv

        os.remove(file[i] + ".csv.gz") #delete ancient file gz

print("You've " + str(num)  + " csv's file ready")
