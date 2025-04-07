import customtkinter as ctk
import NpcFrame as NpcFr
import DungeonFrame as DunFr
import NotesFrame as NotesFr
import TrackerFrame as TrackerFr

class App(ctk.CTk):
    def __init__(self): # Initializer
        super().__init__()
        self.title('Nexus Generator')
        self.geometry('1000x600')
        self.resizable(False, False) 

        self.create_frames()
        self.create_layout()
             
        # Run the main app loop
        self.mainloop()

    def create_frames(self): #create the two main frames for the app
        self.right_frame = RightFrame(self)
        self.left_frame = LeftFrame(self, self.right_frame)
    
    def create_layout(self): #sets the layout for the two main frames
        self.left_frame.place(x=0, y=0, relheight=1.0, relwidth=0.2)
        self.right_frame.place(x=205, y=0, relheight=1.0, relwidth=0.8)

class LeftFrame(ctk.CTkFrame): #contains the bottons to switch between the different app pages
    def __init__(self, master, right_frame):
        super().__init__(master)
        self.place(x=0, y=0, relheight=1.0, relwidth=0.2)
        self.create_widgets(right_frame)
        self.create_layout()

    def create_widgets(self, right_frame): #creates the buttons for the left frame
        self.button_dungeon = ctk.CTkButton(self, 
                                        text="Dungeon Generator", 
                                        command=lambda: right_frame.swap_frame('dungeon'))
        self.button_tracker = ctk.CTkButton(self, 
                                            text="Character Tracker", 
                                            command=lambda: right_frame.swap_frame('tracker'))
        self.button_npc = ctk.CTkButton(self, 
                                        text="NPC Generator", 
                                        command=lambda: right_frame.swap_frame('npc'))

    def create_layout(self): #creates the layout for the buttons in the left frame
        self.button_dungeon.pack(pady=10)
        self.button_tracker.pack(pady=10)
        self.button_npc.pack(pady=10)

class RightFrame(ctk.CTkFrame): #contains the main content of the app, the different pages
    def __init__(self, master):
        super().__init__(master)
        self.place(x=180, y=0, relheight=1.0, relwidth=0.8)

        # Create the notes frame which is always visible on the right side
        self.notes = NotesFr.NotesFrame(self)
        self.notes.pack(side='right', fill='y', pady=10)

        # Create the swappable frames
        self.tracker = TrackerFr.TrackerFrame(self)
        self.character = NpcFr.NpcFrame(self)
        self.dungeon = DunFr.DungeonFrame(self, num_rooms=5)  # Sets the defult number of rooms to 5

    def swap_frame(self, frame): #function to switch between the different pages of the app
        # Hide all swappable frames
        self.tracker.pack_forget()
        self.character.pack_forget()
        self.dungeon.pack_forget()

        # Show the selected frame
        if frame == 'dungeon':
            self.dungeon.pack(side='left', fill='both', expand=True, padx=10, pady=10)
        elif frame == 'tracker':
            self.tracker.pack(side='left', fill='both', expand=True, padx=10, pady=10)
        elif frame == 'npc':
            self.character.pack(side='left', fill='both', expand=True, padx=10, pady=10)
        
App()