import customtkinter as ctk
import NpcFrame as NpcFr
import DungeonFrame as DunFr
import NotesFrame as NotesFr
import TrackerFrame as TrackerFr

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Nexus Generator')
        self.geometry('1000x600')
        self.resizable(False, False) 

        # Create and place the left and right frames
        self.right_frame = RightFrame(self)
        self.left_frame = LeftFrame(self, self.right_frame)

        self.left_frame.place(x=0, y=0, relheight=1.0, relwidth=0.2)
        self.right_frame.place(x=205, y=0, relheight=1.0, relwidth=0.8)

        # Run the main loop
        self.mainloop()

class LeftFrame(ctk.CTkFrame):
    def __init__(self, master, right_frame):
        super().__init__(master)
        self.place(x=0, y=0, relheight=1.0, relwidth=0.2)
        self.create_widgets(right_frame)
        self.create_layout()

    def create_widgets(self, right_frame):
        self.button_dungeon = ctk.CTkButton(self, 
                                        text="Dungeon Generator", 
                                        command=lambda: right_frame.swap_frame('dungeon'))
        self.button_tracker = ctk.CTkButton(self, 
                                            text="Character Tracker", 
                                            command=lambda: right_frame.swap_frame('tracker'))
        self.button_npc = ctk.CTkButton(self, 
                                        text="NPC Generator", 
                                        command=lambda: right_frame.swap_frame('npc'))

    def create_layout(self):
        self.button_dungeon.pack(pady=10)
        self.button_tracker.pack(pady=10)
        self.button_npc.pack(pady=10)

class RightFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.place(x=180, y=0, relheight=1.0, relwidth=0.8)

        # Create the notes frame (always visible)
        self.notes = NotesFr.NotesFrame(self)
        self.notes.pack(side='right', fill='y', pady=10)  # Always visible on the right

        # Create the swappable frames
        self.tracker = TrackerFr.TrackerFrame(self)
        self.npc = NpcFr.NpcFrame(self)
        self.dungeon = DunFr.DungeonFrame(self, num_rooms=5)  # Adjust the number of rooms as needed

    def swap_frame(self, frame):
        # Hide all swappable frames
        self.tracker.pack_forget()
        self.npc.pack_forget()
        self.dungeon.pack_forget()

        # Show the selected frame
        if frame == 'dungeon':
            self.dungeon.pack(side='left', fill='both', expand=True, padx=10, pady=10)
        elif frame == 'tracker':
            self.tracker.pack(side='left', fill='both', expand=True, padx=10, pady=10)
        elif frame == 'npc':
            self.npc.pack(side='left', fill='both', expand=True, padx=10, pady=10)
        
App()

# text box for notes
# inititave tracker
# attack roller for tracker
# general dice roller