import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

#window
window =  ctk.CTk()
window.title("Custom Tkinter App")
window.geometry('600x400')

#widgits
label = ctk.CTkLabel(
    window, 
    text = 'A ctk label', 
    fg_color=('blue','red'), 
    text_color=('black','white'),
    corner_radius=10)
label.pack()

button = ctk.CTkButton(
    window, 
    text = 'A ctk button',
    fg_color = '#FF0',
    text_color='#000',
    hover_color="#AA0",
    command=lambda: ctk.set_appearance_mode('light'))
button.pack()

frame = ctk.CTkFrame(window)
                    
frame.pack()

slider = ctk.CTkSlider(frame)
slider.pack(padx=10, pady=10)

#exersize
switch = ctk.CTkSwitch(
    window,
    text = 'A ctk switch',
    fg_color='red',
    progress_color='pink',
    button_color='green',
    button_hover_color='yellow',
    switch_width=60,
    switch_height=30,
    corner_radius=2)
switch.pack()

#run
window.mainloop()