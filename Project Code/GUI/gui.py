import customtkinter as ctk
import random
import npcGenerator as npc
import dungeonGen as dg

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Nexus Generator')
        self.geometry('1000x600')

        #widgets
        self.right_frame = RightFrame(self)
        self.left_frame = LeftFrame(self, self.right_frame)

        #run
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
        self.npc = NpcFrame(self)
        self.dungeon = DungeonFrame(self, num_rooms=5)  # Adjust the number of rooms as needed

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
        
class NpcFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.generator = npc.NPCGenerator()

        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.health_label = ctk.CTkLabel(self, text='Health Points: ' + str(self.generator.healthPoints))
        self.name_label = ctk.CTkLabel(self, text='Name: ' + self.generator.name)
        self.race_label = ctk.CTkLabel(self, text='Race: ' + self.generator.race)
        self.class_label = ctk.CTkLabel(self, text='Class: ' + self.generator.class_)
        self.alignment_label = ctk.CTkLabel(self, text='Alignment: ' + self.generator.alignment)
        self.gen_button = ctk.CTkButton(self, text='Generate', command=self.generate)

    def create_layout(self):
        self.columnconfigure((0), weight=1, uniform='a')
        self.rowconfigure((0, 1, 2, 3, 4, 5), weight=1, uniform='a')
        self.health_label.grid(row=0, column=0, columnspan=1, sticky='nsew', padx=10, pady=1)
        self.name_label.grid(row=1, column=0, columnspan=1, sticky='nsew', padx=10, pady=1)
        self.race_label.grid(row=2, column=0, columnspan=1, sticky='nsew', padx=10, pady=1)
        self.class_label.grid(row=3, column=0, columnspan=1, sticky='nsew', padx=10, pady=1)
        self.alignment_label.grid(row=4, column=0, columnspan=1, sticky='nsew', padx=10, pady=1)
        self.gen_button.grid(row=5, column=0, columnspan=1, sticky='nsew', padx=10, pady=5)

    def generate(self):
        self.generator.generate_health()
        self.generator.generate_name()
        self.generator.generate_race()
        self.generator.generate_class()
        self.generator.generate_alignment()

        self.update_labels()

    def update_labels(self):
        self.health_label.configure(text='Health Points: ' + str(self.generator.healthPoints))
        self.name_label.configure(text='Name: ' + self.generator.name)
        self.race_label.configure(text='Race: ' + self.generator.race)
        self.class_label.configure(text='Class: ' + self.generator.class_)
        self.alignment_label.configure(text='Alignment: ' + self.generator.alignment)

class DungeonFrame(ctk.CTkFrame):
    def __init__(self, master, num_rooms):
        super().__init__(master)
        self.num_rooms = num_rooms

        self.canvas = ctk.CTkCanvas(self, width=400, height=400, bg="black")
        self.canvas.pack(pady=20)
        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.room_field = ctk.CTkSlider(self, from_=5, to=25, orientation='horizontal', state='normal', number_of_steps=25, command=self.update_label)
        self.room_field.set(self.num_rooms)
        self.room_label = ctk.CTkLabel(self, text=f'Number of Rooms: {self.num_rooms}')
        self.generate_button = ctk.CTkButton(self, text='Generate Dungeon', command=self.regenerate_dungeon)

    def create_layout(self):
        self.room_field.pack(pady=10)
        self.room_label.pack(pady=10)
        self.generate_button.pack(pady=10)

    def update_label(self, value):
        self.num_rooms = int(value)
        self.room_label.configure(text=f'Number of Rooms: {self.num_rooms}')

    def draw_dungeon(self, dungeon):
        self.canvas.delete("all")  # Clear the canvas before drawing
        offset_x, offset_y = 200, 200  # Centering the map
        scale = 75  # Adjust for spacing

        for room in dungeon:
            x, y = room.position
            x, y = x * scale + offset_x, y * scale + offset_y
            
            if room.shape == 'circle':
                self.canvas.create_oval(x-25, y-25, x+25, y+25, fill="white")
            elif room.shape == 'square':
                self.canvas.create_rectangle(x-20, y-20, x+20, y+20, fill="white")

            # Draw connections
            for connected_room in room.connections:
                cx, cy = connected_room.position
                cx, cy = cx * scale + offset_x, cy * scale + offset_y
                self.canvas.create_line(x, y, cx, cy, fill="white", width=7)
            
        for room in dungeon:
            x, y = room.position
            x, y = x * scale + offset_x, y * scale + offset_y
            self.canvas.create_text(x, y, text=str(room.room_id), fill="black", font=("Arial", 12))

    def regenerate_dungeon(self):
        self.draw_dungeon(dg.generate_dungeon(self.num_rooms))

App()
