import os, sys, random, subprocess
import tkinter as tk
from tkinter import filedialog

defaultFolder = "downloadedVideo"
dirPath = ''
videoPrefix = ''
videoSuffix = ''

root = tk.Tk()
root.title('TungThach - Video Downloader')

def runPowerShell(url,prefix,suffix):
    global dirPath, videoPrefix, videoSuffix
    videoPrefix = prefix
    videoSuffix = suffix
    if dirPath == '':
        folder = "C:"
        if os.path.exists(folder + "\\" + defaultFolder):
            pass
        else:
            os.mkdir(folder + "\\" + defaultFolder)
        path1 = folder + "\\" + defaultFolder
        destVar = "$dest=" + "\"" + folder + "\\\"+" + "\"" + defaultFolder + "\\\"+" + "$randomName" + "\n"
    else:
        folder = dirPath
        path1 = folder
        destVar = "$dest=" + "\"" + folder + "\\\"+" + "$randomName" + "\n"

    sourceVar = "$source=" + "\"" + str(url) + "\"" + "\n"
    randomNum = "$randomNumber=Get-Random" + "\n"

    if videoSuffix == '' and videoPrefix == '':
        randomName = "$randomName=[string]$randomNumber +" + "\".mp4\"" + "\n"
    else:
        if videoPrefix != '' and videoSuffix == '':
            randomName = "$randomName="+ "\"" + videoPrefix + "\"+" + "[string]$randomNumber +" + "\".mp4\"" + "\n"
        elif videoSuffix != '' and videoPrefix == '':
            randomName = "$randomName=[string]$randomNumber +" + "\"" + videoSuffix + "\"+" + "\".mp4\"" + "\n"
        elif videoPrefix != '' and videoSuffix != '':
            randomName ="$randomName="+ "\"" + videoPrefix + "\"+" + "[string]$randomNumber +" + "\"" + videoSuffix + "\"+" + "\".mp4\"" + "\n"
    #destVar above
    finalCmd = "Invoke-WebRequest -Uri $source -OutFile $dest" + "\n"

    #randomDir = random.random() + random.random()

    file = open(path1 + "\\" + "VideoDownloader.ps1", "w")
    file.write(sourceVar + randomNum + randomName + destVar + finalCmd)
    file.close()

    executePowershellFile(path1)

def getURL():
    urlVar = e.get()
    prefixName = e1.get()
    suffixName = e2.get()
    finalURL = runPowerShell(urlVar,prefixName,suffixName)

def pathDirectory():
    global dirPath
    dir = filedialog.askdirectory()
    dirPath = dir
    dirPathInfo.config(text=dirPath)
def executePowershellFile(path):
    file_exe = 'powershell -executionpolicy bypass -File ' + path + "\\" + 'VideoDownloader.ps1'
    #subprocess.run(['powershell', "-Command", file_exe])
    subProcessVar = subprocess.Popen(['powershell.exe', file_exe], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
    return subProcessVar

label = tk.Label(root, text="[^_^] Hello [^_^]")
label.config(font=(14))
label.pack()

defaultDir = tk.Label(root, text="Default Directory: C:\\downloadedVideo")
defaultDir.pack()
dirPathInfo = tk.Label(root, text=dirPath, background="pink")
dirPathInfo.pack()

urlLink = tk.Label(root, text="URL---------------------------------------")
urlLink.pack()
e = tk.Entry(root, width=100)
e.pack()

prefixVideoName = tk.Label(root, text="Prefix Video Name ---------------------------------------")
prefixVideoName.pack()
e1 = tk.Entry(root, width=100)
e1.pack()

suffixVideoName = tk.Label(root, text="Suffix Video Name ---------------------------------------")
suffixVideoName.pack()
e2 = tk.Entry(root, width=100)
e2.pack()

buttonDir = tk.Button(root, text="Select Directory Path", command=pathDirectory, background="yellow")
buttonDir.pack()
button = tk.Button(root, text="DOWNLOAD!", command=getURL, background="green")
button.pack()

root.mainloop()
