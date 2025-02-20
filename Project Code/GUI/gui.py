import customtkinter as ctk
import random

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Nexus Generator')
        self.geometry('600x400')

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
        self.button_map = ctk.CTkButton(self, 
                                        text="Map", 
                                        command=lambda: right_frame.swap_frame('map'))
        self.button_monster = ctk.CTkButton(self, 
                                            text="Monster", 
                                            command=lambda: right_frame.swap_frame('monster'))
        self.button_npc = ctk.CTkButton(self, 
                                        text="NPC", 
                                        command=lambda: right_frame.swap_frame('npc'))

    def create_layout(self):
        self.button_map.pack(pady=10)
        self.button_monster.pack(pady=10)
        self.button_npc.pack(pady=10)

class RightFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.place(x=180, y=0, relheight=1.0, relwidth=0.7)

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

class MapFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.temp_label = ctk.CTkLabel(self, text='Map Frame')
        self.temp_label.pack()
        
class MonsterFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.temp_label = ctk.CTkLabel(self, text='Monster Frame')
        self.temp_label.pack()
        
class NpcFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.generator = NPCGenerator()

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
        self.health_label.pack(anchor='w', pady=5)
        self.name_label.pack(anchor='w', pady=5)
        self.race_label.pack(anchor='w', pady=5)
        self.class_label.pack(anchor='w', pady=5)
        self.alignment_label.pack(anchor='w', pady=5)
        self.gen_button.pack(anchor='w', pady=10)

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

class NPCGenerator:
    def __init__(self):
        self.healthPoints = 0
        self.name = ''
        self.race = ''
        self.class_ = ''
        self.alignment = ''

    def generate_health(self):
        self.healthPoints = random.randint(15, 70)
        return self.healthPoints

    def generate_name(self):
        with open('Project Code/GUI/Data Files/first-names.txt', 'r') as file_object:
            list_first_names = file_object.readlines()
            first_name = random.choice(list_first_names).strip()
        with open('Project Code/GUI/Data Files/last-names.txt', 'r') as file_object:
            list_last_names = file_object.readlines()
            last_name = random.choice(list_last_names).strip()
        self.name = first_name + ' ' + last_name
        return self.name

    def generate_race(self):
        with open('Project Code/GUI/Data Files/dnd-races.txt', 'r') as file_object:
            list_races = file_object.readlines()
            self.race = random.choice(list_races).strip()
        return self.race

    def generate_class(self):
        with open('Project Code/GUI/Data Files/dnd-classes.txt', 'r') as file_object:
            list_classes = file_object.readlines()
            self.class_ = random.choice(list_classes).strip()
        return self.class_

    def generate_alignment(self):
        with open('Project Code/GUI/Data Files/dnd-alignments.txt', 'r') as file_object:
            list_alignments = file_object.readlines()
            self.alignment = random.choice(list_alignments).strip()
        return self.alignment

App()
        