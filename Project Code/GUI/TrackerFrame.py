import customtkinter as ctk
import CharacterFrame as NPC
import json
import os

class TrackerFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.npc_data_file = "npc_data.json"  # File to save/load NPC data
        self.create_widgets()
        self.create_layout()
        self.load_npcs()  # Load NPCs when the frame is initialized

    def create_widgets(self):
        self.temp_label = ctk.CTkLabel(self, text='Character Tracker')
        self.add_frame_button = ctk.CTkButton(self, text="Add Frame", command=self.add_new_npc)
        self.clear_roll_button = ctk.CTkButton(self, text="Clear Roll", command=self.clear_roll)
        self.roll_all_button = ctk.CTkButton(self, text="Roll All", command=self.roll_all)
        self.clear_npcs_button = ctk.CTkButton(self, text="Clear NPCs", command=self.clear_npcs)
        # Container for dynamically created frames
        self.frame_container = ctk.CTkScrollableFrame(self)

    def create_layout(self):
        self.temp_label.pack(pady=10)
        self.add_frame_button.pack(pady=10)
        self.frame_container.pack(fill="both", expand=True, padx=10, pady=10)
        self.clear_roll_button.pack(side="left", padx=10, pady=10)
        self.roll_all_button.pack(side="left", padx=10, pady=10)
        self.clear_npcs_button.pack(side="left", padx=10, pady=10)

    def add_new_npc(self):
        """Create a new NPC frame with default values and save it."""
        npc_data = {
            "name": "",
            "health": 0,
            "ac": 0,
            "prof": 0,
            "str": 0,
            "dex": 0,
            "con": 0,
            "int": 0,
            "wis": 0,
            "cha": 0,
        }
        self.create_new_frame(npc_data)
        self.save_npcs()  # Save the new NPC to the file

    def create_new_frame(self, npc_data):
        """Create and pack a new NPC frame with the given data."""
        new_frame = NPC.CharacterFrame(self.frame_container, npc_data, self.save_npcs)  # Pass save callback
        new_frame.pack(fill="x", padx=5, pady=5)

    def save_npcs(self):
        """Save all NPC data to a file."""
        npc_list = []
        for child in self.frame_container.winfo_children():
            if isinstance(child, NPC.CharacterFrame):
                npc_list.append(child.get_npc_data())  # Collect NPC data from each frame

        with open(self.npc_data_file, "w") as file:
            json.dump(npc_list, file, indent=4)

    def load_npcs(self):
        """Load NPC data from a file and create frames for each NPC."""
        if os.path.exists(self.npc_data_file):
            with open(self.npc_data_file, "r") as file:
                npc_list = json.load(file)
                for npc_data in npc_list:
                    self.create_new_frame(npc_data)

    def clear_roll(self):
        """Clear the roll label in all NPC frames."""
        for child in self.frame_container.winfo_children():
            if isinstance(child, NPC.CharacterFrame):
                child.roll_label.configure(text="Roll: -")

    def roll_all(self):
        """Roll for all NPCs and update their labels."""
        for child in self.frame_container.winfo_children():
            if isinstance(child, NPC.CharacterFrame):
                child.roll()
    
    def clear_npcs(self):
        """Clear all NPC frames and reset the data file."""
        for child in self.frame_container.winfo_children():
            child.delete_npc()