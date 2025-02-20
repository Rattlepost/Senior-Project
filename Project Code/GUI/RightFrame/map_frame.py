import customtkinter as ctk

class MapFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.temp_label = ctk.CTkLabel(self, text='Map Frame')
        self.temp_label.pack()