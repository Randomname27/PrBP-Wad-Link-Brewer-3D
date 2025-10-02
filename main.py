# Importing Tkinter module 
from tkinter.ttk import *
import tkinter as tk
from tkinter import messagebox

# Creating root Tkinter window 
root = tk.Tk() 
root.title("PrB+ Wad Link Brewer 3D")
root.geometry("530x250")
root.resizable(False, False)

# Tkinter string variable 
# able to store any string value
wadname_var=tk.StringVar()
wadfile_var=tk.StringVar()
wadauthor_var=tk.StringVar()
waddesc_var=tk.StringVar()
iwadpath_var=tk.StringVar()
var = tk.IntVar()
    
#GREATEST CODE EVER MADE BY RANDOMNAME27 ON GITHUB https://github.com/Randomname27/PrBP-Wad-Link-Brewer-3D

def submit():
    wadname=wadname_var.get()
    wadfile=wadfile_var.get()
    wadauthor=wadauthor_var.get()
    waddesc=waddesc_var.get()
    iwadpath=iwadpath_var.get()
    if var.get() == 1:
        doomiwadname = "DOOM 1"
        doomver = "doom.wad"
    elif var.get() == 2:
        doomiwadname = "DOOM 2"
        doomver = "doom2.wad"
    fullxml = f"""<shortcut>
    <executable>/3ds/PrBoom-Plus.3dsx</executable>
    <arg>-iwad {iwadpath}{doomver} -file {wadfile}</arg>
    <name>{doomiwadname} {wadname} (PrBoom+)</name>
    <description>{waddesc}</description>
    <author>Voxel9, PrBoom+ contributors, {wadauthor} (WAD)</author>
</shortcut>"""
    wadfilef = wadfile.replace(".wad", "")
    xmlfn = f"(PrBoom+) {doomiwadname}_{wadfilef}.xml"
    print(fullxml)
    with open(xmlfn, "w") as f:
        f.write(fullxml)
    messagebox.showinfo('All done', message='XML file created')
    root.destroy()

title_label = tk.Label(root, text = 'PrB+ Wad Link Brewer 3D', font=('calibre',18, 'bold'))
titledesc_label = tk.Label(root, text = 'Lil python script that generates xml files for doom wads with prboom+ to put into the homebrew launcher ', font=('calibre',8, 'italic'))

wadname_label = tk.Label(root, text = 'Wad Name', font=('calibre',10, 'bold'))

wadname_entry = tk.Entry(root,textvariable = wadname_var, font=('calibre',10,'normal'))

wadfile_label = tk.Label(root, text = 'Wad File', font = ('calibre',10,'bold'))

wadfile_entry=tk.Entry(root, textvariable = wadfile_var, font = ('calibre',10,'normal'))

wadauthor_label = tk.Label(root, text = 'Wad Author', font=('calibre',10, 'bold'))

wadauthor_entry = tk.Entry(root,textvariable = wadauthor_var, font=('calibre',10,'normal'))

waddesc_label = tk.Label(root, text = 'Wad Description', font=('calibre',10, 'bold'))

waddesc_entry = tk.Entry(root,textvariable = waddesc_var, font=('calibre',10,'normal'))

iwadpath_label = tk.Label(root, text = 'IWad Path', font=('calibre',10, 'bold'))

iwadpath_entry = tk.Entry(root,textvariable = iwadpath_var, font=('calibre',10,'normal'))

# creating a button using the widget 
# Button that will call the submit function 
sub_btn=tk.Button(root,text = 'Generate', command = submit)

doom1rad = tk.Radiobutton(root, text="Ultimate DOOM",padx=20, variable=var, value=1)
doom2rad = tk.Radiobutton(root, text="DOOM 2", padx=20, variable=var, value=2)
 
# placing the label and entry in
# the required position using grid
# method

title_label.grid(row=0, column=1, pady=(5, 0))
#titledesc_label.grid(row=1,column=0)
doom1rad.grid(row=2,column=0, padx=(20, 0), pady=(10, 10))
doom2rad.grid(row=2,column=2, pady=(10, 10))
wadname_label.grid(row=3,column=0)
wadname_entry.grid(row=3,column=1)
waddesc_label.grid(row=4,column=0)
waddesc_entry.grid(row=4,column=1)
wadauthor_label.grid(row=5,column=0)
wadauthor_entry.grid(row=5,column=1)
wadfile_label.grid(row=6,column=0)
wadfile_entry.grid(row=6,column=1)
iwadpath_label.grid(row=7,column=0)
iwadpath_entry.grid(row=7,column=1)
sub_btn.grid(row=8,column=1, pady=(15, 0))

# Infinite loop can be terminated by 
# keyboard or mouse interrupt 
# or by any predefined function (destroy()) 
tk.mainloop()