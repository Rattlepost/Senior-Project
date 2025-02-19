import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

#setup
window = ctk.CTk()
window.title('Custom Tkinter App')
window.geometry('600x400')

#place
def toggle_label_place():
    global label_visibility
    if label_visibility:
        label.place_forget()
        label_visibility = False
    else:
        label.place(relx=0.5, rely=0.5, anchor='center')
        label_visibility = True

button = ctk.CTkButton(window, text='toggle Label', command=toggle_label_place)
button.place(x=10, y=10)

label_visibility = True
label = ctk.CTkLabel(window, text='A label')
label.place(relx=0.5, rely=0.5, anchor='center')

#run
window.mainloop()