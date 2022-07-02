import os
import sys
import multiprocessing
import math
#test
listWithPaths = "D:\\Ml-Projects\\test"

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
            for pathvgl, filevgl in listWithFiles.items(): 
                if(file == filevgl):
                    dublicatepaths.append(pathvgl) 
        if(len(dublicatepaths) > 1 ): 
            dublicates[file] = dublicatepaths 
        dublicatepaths.clear
        count+= 1
        
    writeintofile(dublicates, "File"+str(i)+".txt")
    print("finished")
    
def writeintofile (listWithDublicates, filename): 
    f= open( filename,"w+", encoding="utf-8")
    for file, list in listWithDublicates.items(): 
            f.write(file)
            for path in list:
                f.write(",")
                f.write(path)
            f.write("\n")
    f.close()

def combinefiles (): 
        with open("results.txt", 'r+', encoding="utf-8") as fout:
            fout.truncate(0)
            fout.close

        for i in range(4):
            with open("results.txt", "r+", encoding="utf-8") as myfile:  
                fout= open( "results.txt","a", encoding="utf-8")    
                f= open( "File"+str(i)+".txt","r", encoding="utf-8")
                Lines = f.readlines()
                test = myfile.readlines()
                for line in Lines:
                    if line not in test:
                        fout.write(line)
                f.close()
                fout.close()  
            myfile.close()
            os.remove("File"+str(i)+".txt")

if __name__  == "__main__":

    with open("results.txt", 'r+', encoding="utf-8") as fout:
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
     
    combinefiles()