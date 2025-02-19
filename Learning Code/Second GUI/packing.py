import customtkinter as ctk

#window
window =  ctk.CTk()
window.title("Custom Tkinter App")
window.geometry('400x600')

#widgets
label1 = ctk.CTkLabel(window, text='A ctk label', fg_color=('blue','red'), text_color=('black','white'))
label2 = ctk.CTkLabel(window, text='A ctk label here', fg_color=('blue','blue'), text_color=('black','white'))
label3 = ctk.CTkLabel(window, text='A ctk', fg_color=('blue','green'), text_color=('black','white'))
button = ctk.CTkButton(window, text='A ctk button', fg_color='white')

#layout
label1.pack(side = 'top', fill = 'x')
label2.pack(side = 'top', expand = True, ipadx = 100)
label3.pack(side = 'top', expand = True, fill = 'both')
button.pack(side = 'top', fill = 'x')

#run
window.mainloop()