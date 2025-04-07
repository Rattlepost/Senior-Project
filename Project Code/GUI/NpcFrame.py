import customtkinter as ctk
import npcGenerator as npc

class NpcFrame(ctk.CTkFrame):
    def __init__(self, master): # Initializer
        super().__init__(master)
        
        self.generator = npc.NPCGenerator()
        self.create_widgets()
        self.create_layout()

    def create_widgets(self): # Create buttons and labels
        self.health_label = ctk.CTkLabel(self, text='Health Points: ' + str(self.generator.healthPoints), anchor='w')
        self.name_label = ctk.CTkLabel(self, text='Name: ' + self.generator.name, anchor='w')
        self.race_label = ctk.CTkLabel(self, text='Race: ' + self.generator.race, anchor='w')
        self.class_label = ctk.CTkLabel(self, text='Class: ' + self.generator.class_, anchor='w')
        self.alignment_label = ctk.CTkLabel(self, text='Alignment: ' + self.generator.alignment, anchor='w')
        self.gen_button = ctk.CTkButton(self, text='Generate', command=self.generate)

    def create_layout(self): # Create the layout for the widgets in a grid format
        self.columnconfigure((0), weight=1, uniform='a')
        self.rowconfigure((0, 1, 2, 3, 4, 5), weight=1, uniform='a')
        self.health_label.grid(row=0, column=0, columnspan=1, sticky='nsew', padx=10, pady=1)
        self.name_label.grid(row=1, column=0, columnspan=1, sticky='nsew', padx=10, pady=1)
        self.race_label.grid(row=2, column=0, columnspan=1, sticky='nsew', padx=10, pady=1)
        self.class_label.grid(row=3, column=0, columnspan=1, sticky='nsew', padx=10, pady=1)
        self.alignment_label.grid(row=4, column=0, columnspan=1, sticky='nsew', padx=10, pady=1)
        self.gen_button.grid(row=5, column=0, columnspan=1, sticky='nsew', padx=10, pady=5)

    def generate(self): # Generate each field for the NPC
        self.generator.generate_health()
        self.generator.generate_name()
        self.generator.generate_race()
        self.generator.generate_class()
        self.generator.generate_alignment()

        self.update_labels()

    def update_labels(self): # Update the labels with the generated values
        self.health_label.configure(text='Health Points: ' + str(self.generator.healthPoints))
        self.name_label.configure(text='Name: ' + self.generator.name)
        self.race_label.configure(text='Race: ' + self.generator.race)
        self.class_label.configure(text='Class: ' + self.generator.class_)
        self.alignment_label.configure(text='Alignment: ' + self.generator.alignment)