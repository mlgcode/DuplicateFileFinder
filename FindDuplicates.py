from audioop import mul
from optparse import Values
import os
import sys
import multiprocessing
import math
import time

start_time = time.time()
listWithPaths = sys.argv[1]

def getAllFiles(path): 
    listWithFiles = {} 
    listoaths = {}
    for path ,subdirs ,files in os.walk ( path ):
        for name in files:
            if name in listWithFiles:
                listWithFiles[name].append(os.path.join(path , name))
            else:
                listoaths = [os.path.join(path , name)]
                listWithFiles[name] = listoaths 
    
    count = 0
    listWithFilesCopy = listWithFiles.copy()
    for key, Values in listWithFilesCopy.items():
        count = count +len(Values)
        if len(Values) < 2:
            listWithFiles.pop(key)
    
    listWithFilesCopy.clear
    
    if listWithFiles:
        print("Files found!") 
    else:
        print("No files found!") 
    writeintofile(listWithFiles)
    
def writeintofile (listWithDublicates): 
    f= open( "results.txt", "a",  encoding="utf-8")
    for file, list in listWithDublicates.items(): 
            f.write(file)
            f.write(",")
            f.write(str(len(list)))
            for path in list:
                f.write(",")
                f.write(path)
            f.write("\n")
    f.close()

if __name__  == "__main__":
    
    with open("results.txt", 'w+', encoding="utf-8") as fout:
        fout.truncate(0)
        fout.close
    
    getAllFiles(listWithPaths)   

    print("--- %s seconds ---" % (time.time() - start_time))
