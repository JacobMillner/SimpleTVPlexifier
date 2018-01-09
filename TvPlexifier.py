import os
from os import listdir
from os.path import isfile, join
from tkinter import *

root = Tk()
root.geometry("600x800")
root.title('Simple TV Plexifier')

#
Label(root, text="First break out the episodes into seasons", fg="Black").grid(row=0)
Label(root, text="by searching which episodes belong to what seasons on TVDB", fg="black").grid(row=1)
#
Label(root, text="Season Directory", bg="grey", fg="white").grid(row=2, column=0)
TbSeason = Text(root, height=1, width=30)
TbSeason.grid(row=2, column=1)
TbSeason.insert(END, "C:\TV\example")
#
Label(root, text="Season Number (XX format)", bg="grey", fg="white").grid(row=3, column=0)
TbNumber = Text(root, height=1, width=30)
TbNumber.grid(row=3, column=1)
TbNumber.insert(END, "06")
#
Label(root, text="TV Show Name", bg="grey", fg="white").grid(row=4, column=0)
TbName = Text(root, height=1, width=30)
TbName.grid(row=4, column=1)
TbName.insert(END, "Sliders")
#
Label(root, text="File Extension", bg="grey", fg="white").grid(row=6, column=0)
TbExt = Text(root, height=1, width=30)
TbExt.grid(row=6, column=1)
TbExt.insert(END, ".mkv")
#
Label(root, text="Next, make sure your episodes are in alphabetical order", fg="Black").grid(row=7)
#
TbLog = Text(root, height=35, width=50, state="normal")
TbLog.grid(row=8, column=0, columnspan=2)
TbLog.insert(END, "[Log]\n")
TbLog.configure(state='disabled')
scrollb = Scrollbar(command=TbLog.yview)
scrollb.grid(row=8, column=1, sticky='nsew')
TbLog['yscrollcommand'] = scrollb.set
#
Button(text="Run", fg="red", height=2, width=10).grid(row=9, column=0)
Button(text="Test", height=2, width=10).grid(row=9, column=1)




mainloop()

#change these vars and run
path = 'H:\TV Shows\Foreign\InuYasha\Season 6'
season = '06'
show = 'InuYasha'
fileExt = '.mkv'

onlyfiles = [f for f in os.listdir(path) if isfile(join(path, f))]

print (onlyfiles)

i = 1
for ep in onlyfiles:
    if i < 10:
        epNum = '0' + str(i)
    else:
        epNum = str(i)
    newfilename = show + ' S' + season + 'E' + epNum + fileExt
    print (newfilename)
    #os.rename(path + '\\' + ep, path + '\\' + newfilename)
    i = i + 1








