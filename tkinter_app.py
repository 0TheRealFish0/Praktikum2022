import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd


############################ CONFIG ##################################
window = tk.Tk(className="Praktikum 2022")
window.geometry("1000x400")

tabControl = ttk.Notebook(window)

tab1 = tk.Frame(tabControl)
tab2 = tk.Frame(tabControl)

tabControl.add(tab1, text="Encrypt Data")
tabControl.add(tab2, text="Decrypt Data")

tabControl.pack(expand = 1, fill ="both")

########################### ENCRYPT TAB ##############################
label = tk.Label(tab1, text="Input for Raw text")
label.pack(padx=3, pady=3)

entry = tk.Entry(tab1, width=80)
entry.pack(padx=3, pady=3)

labelPIN = tk.Label(tab1, text="Your new Pin:")
labelPIN.pack(padx=3, pady=3)
entryPIN = tk.Entry(tab1)
entryPIN.pack(padx=3, pady=3)


def printRawText():
    raw_text = entry.get()
    print(raw_text)

button1 = tk.Button(
    tab1,
    text="Click to submit",
    width=16,
    height=1,
    bg="black",
    foreground="white",
    command=printRawText
).pack(padx=3, pady=3)

########################## DECRYPT TAB #################################

label2 = tk.Label(tab2, text="Select the two files: keyA_enc.bin and file.bin")
label2.pack(padx=3, pady=3)

def selectFile():
    select_file = fd.askopenfilenames(initialdir="/",
                                     title="Select a File")
    
    label2.configure(text=("  &  ".join(select_file)))
    
    print(select_file)

button2 = tk.Button(
    tab2, 
    text="Select File",
    width=16,
    height=1,
    bg="black",
    fg="white",
    command=selectFile
).pack(padx=3, pady=3)


label3 = tk.Label(tab2, text="Insert the Decryption Pin:")
label3.pack(padx=3, pady=3)

entry2 = tk.Entry(tab2)
entry2.pack(padx=3, pady=4)

entry3 = tk.Entry(tab2, width=80)

def decrypt():
    print("decrypting")
    entry3.insert(0, "hi")
    

button3 = tk.Button(
    tab2,
    text="Decrypt Files",
    width=16,
    height=1,
    bg="black",
    fg="white",
    command=decrypt
).pack(padx=3, pady=6)

label4 = tk.Label(tab2, text="Decrypted text:")
label4.pack(padx=3, pady=3)


entry3.pack(padx=3, pady=3)


window.mainloop()