
"""
PROGRAM COMMAND LINE INTERPRETER
YO-SHELL Date: Feb 29,2016
Program done in python 3.5 using spyder IDE
This program will implement a subset of the existing 
bash commands like copy,move,chmod etc that we use

@author:- SaiChowdary Amaraneni
          VishnuChaitanya Mandallapu
          Azharuddin Mohammed
"""

import os
import sys
import shutil
import math
import time

command_history = [] #list to hold all commands

def runShell():
    while True:
        print("in runshell")
        inp= input('parser-$ ') 
        
        parts = inp.split(" ") 
        command_history.append(parts[0]) #collects history
        
        #print(command_history[:])
        if parts[0] == "cp":
           if len(parts)==3:
              copy(parts[1],parts[2])
           else:     #to detect error
               print("Needs 3 arguments")
        elif parts[0]=="mv":
           if len(parts)==3:
              move(parts[1],parts[2])
           else:
               print("Needs 3 arguments")
        elif parts[0]=="rm":
           if len(parts)==2:
              remove(parts[1])
           else:
               print("Needs 2 arguments")
        elif parts[0]=="cat":
           if len(parts)==2:
              cat(parts[1])
           else:
               print("Needs 2 arguments")
        elif parts[0]=="chmod":
            if len(parts)==3:
               changeModify(parts[1],parts[2])
            else:
               print("Needs 3 arguments")
        elif parts[0]=="cd":
            if len(parts)==2:
               cd(parts[1])
            else :
                print("Needs 2 arguments")
        elif parts[0]=="history":
           if len(parts)==1:
              history() 
           else:
               print("Needs only 1 arguments")
        elif parts[0]=="wc":
            if len(parts) > 1:
                if parts[1]=="-l":
                    wcWithFlag(parts[2]) #passing filename
                else:
                    wc(parts[1]) 
            else:
                print("Needs more than 1 argument")
                
        elif parts[0]=="ls":
            if len(parts)==1:
               dir=os.getcwd()
               ls(dir)
            elif parts[1]== "-l":
               ls(dir)
            elif len(parts) > 1:
                if parts[1] == "-s" or "-a" or "-m" or "-c":
                   lsWithFlag(parts[1])
          

#does directory listing
def ls(dir):
    os.listdir(" ")
    for r,d,files in os.walk('.'):
        for f in files:
            print(f)
            print("\n")
    
    #does wordcount in  a file
def wc(file):
    numWords=0
    f=open(file)
    for lines in f:
        words=lines.split(" ")
        numWords=numWords+len(words)
    output="Num of words in "+ file + numWords
    print(output)
    
    #does wordcount and gives num of lines
def wcWithFlag(file):
    numLines=0
    numWords=0
    f=open(file)
    for lines in f:
        words=lines.split(" ")
        numLines=numLines+1
        numWords=numWords+len(words)
    output="Num of words in "+ file + numWords
    print(output)
    output="Num of lines in "+file + numLines
    print(output)
           
    #copies filenames
def copy(first,second):
    shutil.copyfile(first,second) 
    print("file name copied ")
    
    #renames first filename with second
def move(first,second):
    os.rename(first,second)
    print("file name renamed")
        
        #removes file from directory
def remove(first):
    os.remove(first)
    print("file removed")
    # displays the file
def cat(first):
    f = open(first,'r')
    print(f.read())
    #gives permissions to file
def changeModify(num,second):
    print("in chmod func")
    permission=int(num)
    os.chmod(second,permission)
    print("changed permission of")
    print(second)
    print("permission") 
    
    #changes directory 
def cd(newDir):
    try:
       os.chdir(newDir) #given directory
    except:
       print("could find the folder entered")
    if newDir[0]=="..":
       os.chdir(os.newDir.oldpwd(newDir)) #previous directory
    elif newDir[0]=="~":
       os.chdir(os.newDir.expanduser(newDir)) # open home directory
    
def lsWithFlag(first):
    output="\n File Name    Size     Permissions    Accessed      Modified"
    output=+"changed\n"
    output="---------------------------------------------------------------\n"
    os.listdir(" ")
    fileList=[]
    for r,d,files in os.walk('.'):
        for f in files:
            fileList=fileList.append(f)
    for fl in fileList:
        permiss = oct(stat.S_IMODE(os.stat(file).st_mode))
        
    if first == "-s"
       flist.sort(key=lambda fl: fl[7]) 
        
    elif first == "-a"
       flist.sort(key=lambda fl: fl[8]) 
       
    elif first == "-m"
       flist.sort(key=lambda fl: fl[9]) 
    elif first == "-c"
       flist.sort(key=lambda fl: fl[10]) 
       
    output+="\n"fl[0]+"      "+permiss+"      "+fsize+"        "
    output+=time.ctime(fl[8])+"          "+time.ctime(fl[8])+"        "
    output+=time.ctime(fl[10])+"\n"
      
    
    
def history():
    print(command_history[:])
runShell()  
