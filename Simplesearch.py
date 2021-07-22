"""SimpleSearch"""

import webbrowser
from tkinter import *
from tkinter import messagebox

main_window = Tk()
main_window.title('Simple Search')
main_window.geometry("340x120")
main_window.minsize(340, 120)
main_window.maxsize(340, 120)
main_window.config(bg='#628395')
main_window.iconbitmap("data/appbitmap.ico")

text = ""


def search_action(event):
    global text
    text = search_bar.get()
    print(text)
    if text != '':
        webbrowser.open(f"https://www.google.com/search?q={text}")
        search_bar.delete(0, END)


def search_check():
    text = search_bar.get()
    if text != '':
        webbrowser.open(f"https://www.google.com/search?q={text}")
        search_bar.delete(0, END)
    else:
        messagebox.showerror("Nothing to search", "No Input Received")


search_bar = Entry(main_window, width=25, font=('', 14), border=2)
search_bar.pack(pady=10, padx=30)

search_button = Button(main_window, text="Search", border=1, font=('', 12), activebackground='#CDF3A2',
                       activeforeground='#2C2E43', command=search_check)
search_button.pack(pady=10)
search_bar.bind("<Return>", search_action)

main_window.mainloop()
