import customtkinter as ctk

class LeftFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.button_map = ctk.CTkButton(self, 
                                        text="Map", 
                                        command=lambda: master.right_frame.swap_frame('map'))
        self.button_monster = ctk.CTkButton(self, 
                                            text="Monster", 
                                            command=lambda: master.right_frame.swap_frame('monster'))
        self.button_npc = ctk.CTkButton(self, 
                                        text="NPC", 
                                        command=lambda: master.right_frame.swap_frame('npc'))

        self.button_map.pack(pady=10)
        self.button_monster.pack(pady=10)
        self.button_npc.pack(pady=10)