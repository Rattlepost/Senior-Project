import customtkinter as ctk
import NpcFrame as NpcFr
import DungeonFrame as DunFr

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Nexus Generator')
        self.geometry('1000x600')

        # Create and place the left and right frames
        self.right_frame = RightFrame(self)
        self.left_frame = LeftFrame(self, self.right_frame)

        self.left_frame.place(x=0, y=0, relheight=1.0, relwidth=0.3)
        self.right_frame.place(x=300, y=0, relheight=1.0, relwidth=0.7)

        # Run the main loop
        self.mainloop()

class LeftFrame(ctk.CTkFrame):
    def __init__(self, master, right_frame):
        super().__init__(master)
        self.place(x=0, y=0, relheight=1.0, relwidth=0.3)
        self.create_widgets(right_frame)
        self.create_layout()

    def create_widgets(self, right_frame):
        self.button_dungeon = ctk.CTkButton(self, 
                                        text="Dungeon", 
                                        command=lambda: right_frame.swap_frame('dungeon'))
        self.button_monster = ctk.CTkButton(self, 
                                            text="Monster", 
                                            command=lambda: right_frame.swap_frame('monster'))
        self.button_npc = ctk.CTkButton(self, 
                                        text="NPC", 
                                        command=lambda: right_frame.swap_frame('npc'))

    def create_layout(self):
        self.button_dungeon.pack(pady=10)
        self.button_monster.pack(pady=10)
        self.button_npc.pack(pady=10)

class RightFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.place(x=180, y=0, relheight=1.0, relwidth=0.7)

        self.monster = MonsterFrame(self)
        self.npc = NpcFr.NpcFrame(self)
        self.dungeon = DunFr.DungeonFrame(self, num_rooms=5)  # Adjust the number of rooms as needed

    def swap_frame(self, frame):
        self.monster.pack_forget()
        self.npc.pack_forget()
        self.dungeon.pack_forget()

        if frame == 'dungeon':
            self.dungeon.pack(fill='both', expand=True)
        elif frame == 'monster':
            self.monster.pack(fill='both', expand=True)
        elif frame == 'npc':
            self.npc.pack(fill='both', expand=True)
        
class MonsterFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.temp_label = ctk.CTkLabel(self, text='Monster Frame')
        self.temp_label.pack()
        
App()

# text box for notes
# inititave tracker
# attack roller for combat
# general dice roller