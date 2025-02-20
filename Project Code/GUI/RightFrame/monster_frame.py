import customtkinter as ctk

class MonsterFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.temp_label = ctk.CTkLabel(self, text='Monster Frame')
        self.temp_label.pack()