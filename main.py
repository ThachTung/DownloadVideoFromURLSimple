import os, sys, random, subprocess
import tkinter as tk
import multiprocessing
from multiprocessing import Process, freeze_support

defaultFolder = "downloadedVideo"
videoFolder ="_video"

root = tk.Tk()
root.title('TungThach - Optional')

checkValue = tk.IntVar()
globalCheck = 1

def checkClicked():
    global globalCheck
    if checkValue.get():
        globalCheck = 0
    else:
        globalCheck = 1

def runPowerShell(url):
    if globalCheck == 0:
        folder = "D:"
    else:
        folder = "C:"

    if os.path.exists(folder + "\\" + defaultFolder) or os.path.exists(folder + "\\" + defaultFolder + "\\" + videoFolder) :
        pass
    else:
        os.mkdir(folder + "\\" + defaultFolder)
        os.mkdir(folder + "\\" + defaultFolder + "\\" + videoFolder)

    sourceVar = "$source=" + "\"" + str(url) + "\"" + "\n"
    randomNum = "$randomNumber=Get-Random" + "\n"
    randomName = "$randomName=[string]$randomNumber" + "+" + "\".mp4\"" + "\n"
    destVar = "$dest=" + "\"" + folder + "\\\"+" + "\"" + defaultFolder + "\\\"+" + "\"_video\\\"+" + "$randomName" + "\n"
    finalCmd = "Invoke-WebRequest -Uri $source -OutFile $dest" + "\n"


    randomDir = random.random() + random.random()
    path1 = folder + "\\" + defaultFolder + "\\" + str(randomDir)
    os.mkdir(path1)

    file = open(path1 + "\\" + "VideoDownloader.ps1", "w")
    file.write(sourceVar + randomNum + randomName + destVar + finalCmd)
    file.close()

    executePowershellFile(path1)


def getURL():
    urlVar = e.get()
    finalURL = runPowerShell(urlVar)

def executePowershellFile(path):
    file_exe = 'powershell -executionpolicy bypass -File ' + path + "\\" + 'VideoDownloader.ps1'
    #subprocess.run(['powershell', "-Command", file_exe])
    subProcessVar = subprocess.Popen(['powershell.exe', file_exe], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
    return subProcessVar

label = tk.Label(root, text="[^_^] Hello [^_^]")
label.config(font=(14))
label.pack()
checkBut = tk.Checkbutton(root, text='D Directory', variable=checkValue,
                onvalue=1, offvalue=0, command=checkClicked)
checkBut.pack()
dirInfo = tk.Label(root, text="Directory After Click Button: C:\\downloadedVideo \n Directory If D Was Checked: D:\\downloadedVideo")
dirInfo.pack()
e = tk.Entry(root, width=100)
e.pack()
button = tk.Button(root, text="Click Here Please!", command=getURL)
button.pack()

root.mainloop()