import os
import sys
import multiprocessing
import math

listWithPaths = sys.argv[1]

def getAllFiles(path): 
    listWithFiles = {} 
    for path ,subdirs ,files in os.walk ( path ):
        for name in files:
            listWithFiles[os.path.join(path , name)] = name 
    print("Files found!") 
    return listWithFiles

def findDuplicates (listWithFiles, i): 
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
    for path, file in listWithFiles.items(): 
        dublicatepaths = [] 
        if count >= start and count < end:
            with open("results.txt", "r+", encoding="utf-8") as myfile:  
                text = myfile.read()
                if file not in text:
                    for pathvgl, filevgl in listWithFiles.items(): 
                        if(file == filevgl):
                            dublicatepaths.append(pathvgl) 
            myfile.close
        if(len(dublicatepaths) > 1 ): 
            dublicates[file] = dublicatepaths 
        dublicatepaths.clear
        count+= 1
        
    writeintofile(dublicates)
    print("finished")
    
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
  
    foundFiles = []
    for i in range(4):
        p = multiprocessing.Process(target=findDuplicates, args=(listWithFiles, i))
        foundFiles.append(p)
        p.start()
        
    for file in foundFiles:
        file.join()  
