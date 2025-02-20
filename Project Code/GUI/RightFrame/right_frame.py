import customtkinter as ctk
from RightFrame.map_frame import MapFrame
from RightFrame.monster_frame import MonsterFrame
from RightFrame.npc_frame import NpcFrame

class RightFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.map = MapFrame(self)
        self.monster = MonsterFrame(self)
        self.npc = NpcFrame(self)

    def swap_frame(self, frame):
        self.map.pack_forget()
        self.monster.pack_forget()
        self.npc.pack_forget()

        if frame == 'map':
            self.map.pack(fill='both', expand=True)
        elif frame == 'monster':
            self.monster.pack(fill='both', expand=True)
        elif frame == 'npc':
            self.npc.pack(fill='both', expand=True)