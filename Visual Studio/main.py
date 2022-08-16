import tkinter
import os
from tkinter import filedialog

separationString = "\nO"  #string used to mark the start of a new file

tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing

filePath = filedialog.askopenfile()
fileName = os.path.basename(filePath.name)
extension = fileName.split(".")[-1]
fileParentPath = os.path.dirname(filePath.name)
print(fileParentPath)
with open(filePath.name) as file:   #open file
    data = file.read()  #get data from file

data = data.split(separationString) #split data based on separation string

saveFolderName = fileName.replace("." + extension, "") + " split files"
saveFolderPath = os.path.join(fileParentPath, saveFolderName)

os.mkdir(saveFolderPath)

for index, fileData in enumerate(data):
    subFileName = fileName + " " + str(index) + "." + extension
    if(index != 0):
        fileData = separationString + fileData
    with open(os.path.join(saveFolderPath, subFileName), "w") as subFile:   #create new sub file
        subFile.write(fileData.strip())
