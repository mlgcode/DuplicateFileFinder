from ast import And, Index
import os
import sys

listWithPaths = [sys.argv[1]]

def main ( listWithPaths ) : 
    listwithFiles = getAllFiles(listWithPaths) 
    listWithDublicates = findDuplicates(listwithFiles) 
    listwithFiles.clear 
    print ( " Liste : " ) 
    print ( listWithDublicates ) 
   
def getAllFiles(list): 
    listWithFiles = {} 
    
    for targetPath in list: 
        for path ,subdirs ,files in os.walk ( targetPath ):
            for name in files:
                listWithFiles[os.path.join(path , name)] = name 
    print("Files found!") 
    return listWithFiles 

def findDuplicates (listWithFiles): 
    dublicates = {} 
    counter = 0
    percentage = 0
    for path, file in listWithFiles.items(): 
        counter = 0
        for pathvgl , filevgl in listWithFiles.items(): 
            if(file == filevgl):
                counter+=1
        if(counter > 1 ): 
            dublicates[file] = counter 
            percentage += 1
        if(percentage > 200):
            percentage = list(listWithFiles.keys()).index(path) / len(listWithFiles)
            print(percentage)
            percentage = 0
    return dublicates 



if __name__  == "__main__":
   main(listWithPaths)