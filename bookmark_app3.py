# GUI Graphical User Interface

import tkinter as tk
import webbrowser as wb
import os


def	open_gm(event):
	wb.open_new_tab("https://mail.google.com/mail/u/0/#inbox")

def open_gh(event):
	wb.open_new_tab("https://github.com/VictorCabrejos")
def open_rp(event):
	wb.open_new_tab("http://v-beta.urp.edu.pe/posgrado/maestrias/ingenieria-informatica-con-mencion-en-ingenieria-de-software")

def open_dl(event):
	path = r'D:\SSD\Python Ebooks\00 - MACHINE LEARNING - DEEP LEARNING\DL - Grokking Deep Learning by Andrew Trask (2018)'
	filename=r"\Grokking Deep Learning by Andrew Trask.pdf"
	os.startfile(path+filename)
def open_pe(event):
	path = r'C:\Users\vmc62\Desktop\RICARDO PALMA'
	filename=r"\Plan de Estudios RP.png"
	os.startfile(path+filename)

window = tk.Tk()

window.geometry("800x400")

window.rowconfigure(0, weight=1)
window.rowconfigure(5, weight=1)
window.columnconfigure(0, weight=1)
window.columnconfigure(5, weight=1)

label1 = tk.Label(text="Click to Open a Site", font="none 16 bold")
label1.grid(row=1, column=1, columnspan=3, pady=20)

button1 = tk.Button(text="Gmail", bg="blue", fg="white", font="none 16 bold", relief="raised")
button1.grid(row=2, column=1, pady=10)

button2 = tk.Button(text="Github", bg="red", fg="white", font="none 16 bold", relief="raised")
button2.grid(row=2, column=2, pady=10)

button3 = tk.Button(text="Ricardo Palma", bg="green", fg="white", font="none 16 bold", relief="raised")
button3.grid(row=2, column=3, pady=10)

button1.bind("<Button-1>", open_gm)
button2.bind("<Button-1>", open_gh)
button3.bind("<Button-1>", open_rp)

#*****************
label2 = tk.Label(text="Click to Open a File", font="none 16 bold")
label2.grid(row=3, column=1, columnspan=3, pady=20)

button4 = tk.Button(text="Deep Learning", bg="blue", fg="white", font="none 16 bold", relief="raised")
button4.grid(row=4, column=1 , padx=20, pady=10)

button5 = tk.Button(text="Plan de Estudios", bg="red", fg="white", font="none 16 bold", relief="raised")
button5.grid(row=4, column=3, padx=20, pady=10)

button4.bind("<Button-1>", open_dl)
button5.bind("<Button-1>", open_pe)

window.mainloop()