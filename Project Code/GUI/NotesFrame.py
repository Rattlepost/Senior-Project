import customtkinter as ctk

class NotesFrame(ctk.CTkFrame):
    def __init__(self, master): # Initializer
        super().__init__(master)

        self.create_widgets()
        self.create_layout()

    def create_widgets(self): # Create the widgets for the notes frame
        self.notes_label = ctk.CTkLabel(self, text='Notes')
        self.ctk_textbox = ctk.CTkTextbox(self, width=300, height=200)

    def create_layout(self): # Create the layout for the notes frame
        self.notes_label.pack()
        self.ctk_textbox.pack(pady=10, padx=10, fill='both', expand=True)