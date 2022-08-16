import tkinter
import os
from tkinter import filedialog

separationString = "\nO"  #string used to mark the start of a new file

tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing

filePath = filedialog.askopenfile()     #select file to split

#find file name, extension, and parent directory
fileName = os.path.basename(filePath.name)
extension = fileName.split(".")[-1]
fileParentPath = os.path.dirname(filePath.name)

#TODO: do some input file varification to be sure it is a text file and is an expected size

with open(filePath.name) as file:   #open main file
    data = file.read()  #get data from file

data = data.split(separationString) #split data based on separation string

#create name and path for new folder to store split files
saveFolderName = fileName.replace("." + extension, "") + " split files"
saveFolderPath = os.path.join(fileParentPath, saveFolderName)

#TODO: handle folder already existiong(currently just fails and exits)
os.mkdir(saveFolderPath)    #make folder to contain new files

for index, fileData in enumerate(data): #loop through split file data

    #TODO: use data from files to create more descriptive names
    subFileName = fileName + " " + str(index) + "." + extension     #create a name for each new file, currently just original filename with an index

    if(index != 0):
        fileData = separationString + fileData      #add separation string back onto the beginning of each file after the first(.split removes it)

    with open(os.path.join(saveFolderPath, subFileName), "w") as subFile:       #create new sub file
        subFile.write(fileData.strip())      #remove whitespace at ends and write file
