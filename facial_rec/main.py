from tkinter import *
from auth import *
from math import pow
import random
import hashlib
import time
import json

window = Tk()
window.attributes('-fullscreen',True)
w = window.winfo_screenwidth()
h = window.winfo_screenheight()
#window.geometry("%dx%d+100+100" % (w, h))
window.title("Welcome to NIS Bank")
window.configure(background = "gray7")

def register():
    def addtoDir():
        newWin = Toplevel(window)
        newWin.attributes('-fullscreen',True)
        newWin.title("Authentication")
        newWin.configure(background = "gray7")
        Label(
            newWin,
            text = " Welcome to NIS Bank ",
            bg = "gray7",
            fg = "White",
            font = "Consolas 72"
        ).place(
            x = 210,
            y = 50
        )
        Nm = NameEntry.get()
        Pn = NPINEntry.get()
        NameEntry.delete(0,END)
        NPINEntry.delete(0,END)
        if len(Pn) == 4 and Pn.isdigit():
            q = 123456789987654321234567898
            #random.randint(pow(10,20),pow(10,50))
            g = 23931164504956447807213117212663825326210289577470
            key = gen_key(q) #Receiver_Private_key
            h = power(g,key,q)
            en_msg, p, out = encrypt(Pn,q,h,g)
            dr_msg = decrypt(en_msg,p,key,q)
            dmsg = ''.join(dr_msg)
            print("Decrypted Message: ",dmsg)
            new_data = {out: Nm}
            
            with open('hashDir.json', 'r') as f:
                json_dict = json.load(f)
            json_dict.update(new_data)
            with open('hashDir.json', 'w') as f:
                f.write(json.dumps(json_dict))

            Label(
                newWin,
                text = "Registration Successful" + Nm + "!",
                bg = "gray7",
                fg = "White",
                font = "Consolas 20"
            ).place(
                x = 550,
                y = 300
            )
            Button(
                newWin,
                text = "Back",
                width = 20,
                font = "Calibri 15",
                bg = "gray88",
                fg = "Black",
                command = newWin.destroy
            ).place(
                x = 650,
                y = 425
            )
        else:
            Label(
                newWin,
                text = "Invalid PIN. Please set 4 digit PIN.",
                bg = "gray7",
                fg = "White",
                font = "Consolas 20"
            ).place(
                x = 510,
                y = 300
            )
            Button(
                newWin,
                text = "Back",
                width = 20,
                font = "Calibri 15",
                bg = "gray88",
                fg = "Black",
                command = newWin.destroy
            ).place(
                x = 650,
                y = 425
            )
            
    newWin = Toplevel(window)
    newWin.attributes('-fullscreen',True)
    newWin.title("Authentication")
    newWin.configure(background = "gray7")
    Label(
        newWin,
        text = " Welcome to NIS Bank ",
        bg = "gray7",
        fg = "White",
        font = "Consolas 72"
    ).place(
        x = 210,
        y = 50
    )
    Label(
        newWin,
        text = "Enter your Name:",
        bg = "gray7",
        fg = "White",
        font = "SegoeUILight 20",
    ).place(
        x = 635,
        y = 250
    )
    NameEntry = Entry(
        newWin,
        #window,
        width = 15,
        font = "Consolas 50",
    )
    NameEntry.place(
        x = 480,
        y = 300
    )
    NameEntry.focus_set()
    Label(
        newWin,
        text = "Set your 4-digit PIN:",
        bg = "gray7",
        fg = "White",
        font = "SegoeUILight 20",
    ).place(
        x = 630,
        y = 425
    )
    NPINEntry = Entry(
        newWin,
        #window,
        width = 4,
        font = "Consolas 50",
        show = "*"
    )
    NPINEntry.place(
        x = 682,
        y = 475
    )
    NPINEntry.focus_set()
    Button(
        newWin,
        #window,
        text = "Proceed",
        width = 20,
        font = "Calibri 15",
        bg = "gray88",
        fg = "Black",
        command = addtoDir
    ).place(
        x = 650,
        y = 600
    )
    Button(
        newWin,
        text = "Back",
        width = 20,
        font = "Calibri 15",
        bg = "gray88",
        fg = "Black",
        command = newWin.destroy
    ).place(
        x = 650,
        y = 650
    )

def login():
    def authenticate():
        newWin = Toplevel(window)
        newWin.attributes('-fullscreen',True)
        newWin.title("Authentication")
        newWin.configure(background = "gray7")
        Label(
            newWin,
            text = " Welcome to NIS Bank ",
            bg = "gray7",
            fg = "White",
            font = "Consolas 72"
        ).place(
            x = 210,
            y = 50
        )
        P = PINEntry.get()
        PINEntry.delete(0,END)
        if len(P) == 4 and P.isdigit():
            q = 123456789987654321234567898
            #random.randint(pow(10,20),pow(10,50))
            g = 23931164504956447807213117212663825326210289577470
            key = gen_key(q) #Receiver_Private_key
            h = power(g,key,q)
            en_msg, p, out = encrypt(P,q,h,g)
            dr_msg = decrypt(en_msg,p,key,q)
            dmsg = ''.join(dr_msg)
            print("Decrypted Message: ",dmsg)
            flag = 0
            with open("hashDir.json", "r+") as file:
                hashDir = json.load(file)
            hashDirLen = len(hashDir)
            hashList = list(hashDir.keys())
            for i in range(len(hashList)):
                if out == hashList[i]:
                    flag = 1
                    pos = i
                    break
            if flag == 1:
                Label(
                    newWin,
                    text = "PIN Matched. Hello, " + hashDir[hashList[pos]] + "!",
                    bg = "gray7",
                    fg = "White",
                    font = "Consolas 20"
                ).place(
                    x = 550,
                    y = 300
                )
                Button(
                    newWin,
                    text = "Back",
                    width = 20,
                    font = "Calibri 15",
                    bg = "gray88",
                    fg = "Black",
                    command = newWin.destroy
                ).place(
                    x = 650,
                    y = 425
                )
            else:
                Label(
                    newWin,
                    text = "No match found. Please try again.",
                    bg = "gray7",
                    fg = "White",
                    font = "Consolas 20"
                ).place(
                    x = 530,
                    y = 300
                )
                Button(
                    newWin,
                    text = "Back",
                    width = 20,
                    font = "Calibri 15",
                    bg = "gray88",
                    fg = "Black",
                    command = newWin.destroy
                ).place(
                    x = 650,
                    y = 425
                )
        else:
            Label(
                newWin,
                text = "Invalid PIN. Please try again.",
                bg = "gray7",
                fg = "White",
                font = "Consolas 20"
            ).place(
                x = 530,
                y = 300
            )
            Button(
                newWin,
                text = "Back",
                width = 20,
                font = "Calibri 15",
                bg = "gray88",
                fg = "Black",
                command = newWin.destroy
            ).place(
                x = 650,
                y = 425
            )
            Button(
                window,
                text = "Quit",
                width = 20,
                font = "Calibri 15",
                bg = "gray88",
                fg = "Black",
                command = window.destroy
            ).place(
                x = 650,
                y = 475
            )

    newWin = Toplevel(window)
    newWin.attributes('-fullscreen',True)
    newWin.title("Authentication")
    newWin.configure(background = "gray7")
    Label(
        newWin,
        text = " Welcome to NIS Bank ",
        bg = "gray7",
        fg = "White",
        font = "Consolas 72"
    ).place(
        x = 210,
        y = 50
    )
    Label(
        newWin,
        text = "Enter your 4-digit PIN:",
        bg = "gray7",
        fg = "White",
        font = "SegoeUILight 20",
    ).place(
        x = 625,
        y = 250
    )
    PINEntry = Entry(
        newWin,
        #window,
        width = 4,
        font = "Consolas 50",
        show = "*"
    )
    PINEntry.place(
        x = 682,
        y = 300
    )
    PINEntry.focus_set()
    Button(
        newWin,
        #window,
        text = "Proceed",
        width = 20,
        font = "Calibri 15",
        bg = "gray88",
        fg = "Black",
        command = authenticate
    ).place(
        x = 650,
        y = 425
    )
    Button(
        newWin,
        text = "Back",
        width = 20,
        font = "Calibri 15",
        bg = "gray88",
        fg = "Black",
        command = newWin.destroy
    ).place(
        x = 650,
        y = 475
    )
  
Label(
    text = " Welcome to NIS Bank ",
    bg = "gray7",
    fg = "White",
    font = "Consolas 72"
).place(
    x = 210,
    y = 70
)
Label(
    text = "New User?",
    bg = "gray7",
    fg = "White",
    font = "SegoeUILight 20",
).place(
    x = 680,
    y = 250
)
Button(
    window,
    text = "Yes",
    width = 20,
    font = "Calibri 15",
    bg = "gray88",
    fg = "Black",
    command = register
).place(
    x = 650,
    y = 375
)
Button(
    window,
    text = "No",
    width = 20,
    font = "Calibri 15",
    bg = "gray88",
    fg = "Black",
    command = login
).place(
    x = 650,
    y = 425
)
Button(
    window,
    text = "Quit",
    width = 20,
    font = "Calibri 15",
    bg = "gray88",
    fg = "Black",
    command = window.destroy
).place(
    x = 650,
    y = 475
)
window.mainloop()
