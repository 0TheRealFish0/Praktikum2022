import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA256



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
    
    data = entry.get()
    data = bytes(data, 'utf-8')

    ####################### keyA ##########################################


    keyA = get_random_bytes(32)

    print("keyA: ", keyA)

    cipher = AES.new(keyA, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    file_out = open("file.bin", "wb")
    for x in (cipher.nonce, tag, ciphertext):
        file_out.write(x)
    file_out.close()

    
    pin = entryPIN.get()
    hashedPin = SHA256.new(data=bytes(str(pin), 'utf-8'))
    print("hash: ", hashedPin.digest())


    data2 = keyA

    keyB = hashedPin.digest()

    cipher2 = AES.new(keyB, AES.MODE_GCM)
    ciphertext2, tag2 = cipher2.encrypt_and_digest(data2)

    file_out2 = open("keyA_enc.bin", "wb")

    for x in (cipher2.nonce, tag2, ciphertext2):
        file_out2.write(x)

    file_out2.close()


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

label5 = tk.Label(tab2, text="Select FIRST file.bin, THEN keyA_enc.bin")
label5.pack(padx=3, pady=3)

def selectFile():
    select_file = fd.askopenfilenames(initialdir="/",
                                     title="Select a File")
    
    label2.configure(text=("  &  ".join(select_file)))
    print(select_file)

    global file1
    global file2
    file1, file2 = select_file



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
    UserInput_hashed = SHA256.new(data=bytes(str(entry2), 'utf-8'))
    print(UserInput_hashed.digest())
    
    try:
        file_in = open(file2, "rb")
        nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]
        print("stage 1 done")
        cipher = AES.new(UserInput_hashed.digest(), AES.MODE_GCM, nonce)
        data = cipher.decrypt_and_verify(ciphertext, tag)

        print(data)
        
        file_in2 = open(file1, "rb")
        nonce2, tag2, ciphertext2 = [ file_in2.read(x) for x in (16, 16, -1) ]

        cipher2 = AES.new(data, AES.MODE_GCM, nonce2)
        
        global data2
        data2 = cipher2.decrypt_and_verify(ciphertext2, tag2)

        entry3.insert(data2.decode("utf-8"))
        print(data2.decode("utf-8"))
        print()
        

    except ValueError:
        print("wrong pin")
    

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