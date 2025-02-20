import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self, title, size):

        #main setup
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(600, 600)

        #widgets
        self.menu = Menu(self)
        self.main = Main(self)

        #run
        self.mainloop()

class Menu(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)
        self.place(x=0, y=0, relheight=1.0, relwidth=0.3)
        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.menu_button1 = ctk.CTkButton(self, text='Button 1')
        self.menu_button2 = ctk.CTkButton(self, text='Button 2')
        self.menu_button3 = ctk.CTkButton(self, text='Button 3')

        self.menu_slider1 = ctk.CTkSlider(self, orientation='vertical')
        self.menu_slider2 = ctk.CTkSlider(self, orientation='vertical')

        self.toggle_frame = ctk.CTkFrame(self)
        self.menu_toggle1 = ctk.CTkCheckBox(self.toggle_frame, text='check 1')
        self.menu_toggle2 = ctk.CTkCheckBox(self.toggle_frame, text='check 2')

        self.entry = ctk.CTkEntry(self)
    
    def create_layout(self):
        #create grid
        self.columnconfigure((0, 1, 2), weight=1, uniform='a')
        self.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform='a')

        #place widgets
        self.menu_button1.grid(row=0, column=0, sticky='nswe', columnspan=2)
        self.menu_button2.grid(row=0, column=2, sticky='nswe')
        self.menu_button3.grid(row=1, column=0, columnspan=3, sticky='nsew')

        self.menu_slider1.grid(row=2, column=0, rowspan=2, sticky='nsew', pady=20)
        self.menu_slider2.grid(row=2, column=2, rowspan=2, sticky='nsew', pady=20)

        #toggle layout
        self.toggle_frame.grid(row=4, column=0, columnspan=3, sticky='nsew')
        self.menu_toggle1.pack(side='left', expand=True)
        self.menu_toggle2.pack(side='left', expand=True)

        #entry layout
        self.entry.grid(row=5, column=0, columnspan=3, sticky='nsew', pady=10)

class Main(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.place(relx=0.3, y=0, relheight=1.0, relwidth=0.7)

        Entry(self, 'Test1', 'Button 1', 'red')
        Entry(self, 'Test2', 'Button 2', 'green')
        
class Entry(ctk.CTkFrame):
    def __init__(self, master, label_text, button_text, label_color):
        super().__init__(master)
        self.place(relx=0.3, y=0, relheight=1.0, relwidth=0.7)
    
        label = ctk.CTkLabel(self, text=label_text, bg_color=label_color)
        button = ctk.CTkButton(self, text=button_text)

        label.pack(fill='both', expand=True)
        button.pack(fill='both', expand=True)

        self.pack(side='left', expand=True, fill='both', padx=20, pady=20)

App('Class Practice App', (600, 600))