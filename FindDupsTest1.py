from audioop import mul
import os
import sys
import multiprocessing
import math
import time

start_time = time.time()
listWithPaths = "/media/michel/Tosh FP_6"

def getAllFiles(path): 
    count = 0
    listWithFiles = {} 
    for path ,subdirs ,files in os.walk ( path ):
        for name in files:
            count+=1
            listWithFiles[os.path.join(path , name)] = name 
    if listWithFiles:
        print("Files found!") 
    else:
        print("No files found!") 
    return listWithFiles

def findDuplicates (listWithFiles, i, alradyAdded): 
    dublicates = {}
    switcher = {
        0: 0,
        1: 0.25,
        2: 0.5,
        3: 0.75,
    } 
    
    start = math.floor(len(listWithFiles)*(switcher.get(i)))
    end = math.ceil(len(listWithFiles)*((switcher.get(i))+0.25))

    count = 0
    test = alradyAdded[:]

    for path, file in listWithFiles.items(): 
        dublicatepaths = [] 
        if count >= start and count < end:
            if count not in test:
                for pathvgl, filevgl in listWithFiles.items(): 
                    if(file == filevgl):
                        dublicatepaths.append(pathvgl) 
                        alradyAdded[count] = count
        else: 
            count+= 1
            continue

        if(len(dublicatepaths) > 1 ): 
            dublicates[file] = dublicatepaths 
        dublicatepaths.clear
        count+= 1
    
    count123 = 0
    listWithFilesCopy = dublicates.copy()
    for key, Values in dublicates.items():
        if len(Values) < 2:
            del listWithFiles[key]
            count123+=1
    print(count123)
    writeintofile(dublicates)
    print("finished:"+"i:"+ str(i) + ":"+ str(len(dublicates)))
    
def writeintofile (listWithDublicates): 
    f= open( "results.txt", "a",  encoding="utf-8")
    for file, list in listWithDublicates.items(): 
            f.write(file)
            for path in list:
                f.write(",")
                f.write(path)
            f.write("\n")
    f.close()

if __name__  == "__main__":
    
    with open("results.txt", 'w+', encoding="utf-8") as fout:
        fout.truncate(0)
        fout.close
    
    listWithFiles = getAllFiles(listWithPaths)   
    alradyused = multiprocessing.Array('i', len(listWithFiles))

    foundFiles = []
    for i in range(4):
        p = multiprocessing.Process(target=findDuplicates, args=(listWithFiles, i, alradyused))
        foundFiles.append(p)
        p.start()

    for file in foundFiles:
        file.join() 
    print("--- %s seconds ---" % (time.time() - start_time))
