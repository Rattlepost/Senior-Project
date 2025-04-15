import customtkinter as ctk
import npcGenerator as npc
from threading import Thread


class NpcFrame(ctk.CTkFrame):
    def __init__(self, master):  # Initializer
        super().__init__(master)

        self.generator = npc.NPCGenerator()
        self.create_widgets()
        self.create_layout()

    def create_widgets(self):  # Create buttons, labels, and dropdown menus
        # Group NPC info in a frame
        self.info_frame = ctk.CTkFrame(self)
        self.info_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # NPC attributes
        self.health_label = ctk.CTkLabel(
            self.info_frame, text="Health Points: ", anchor="w"
        )
        self.name_label = ctk.CTkLabel(self.info_frame, text="Name: ", anchor="w")
        self.race_label = ctk.CTkLabel(self.info_frame, text="Race: ", anchor="w")
        self.class_label = ctk.CTkLabel(self.info_frame, text="Class: ", anchor="w")
        self.alignment_label = ctk.CTkLabel(
            self.info_frame, text="Alignment: ", anchor="w"
        )

        # Buttons
        self.gen_button = ctk.CTkButton(self, text="Generate", command=self.start_gen)

        # Dropdown container
        self.dropdown_frame = ctk.CTkFrame(self)

        # Textbox for additional information
        self.info_textbox = ctk.CTkTextbox(
            self, width=400, height=300, wrap="word", font=("Arial", 14)
        )
        self.info_textbox.insert("1.0", "")
        self.info_textbox.configure(state="disabled")  # Make it read-only

    def create_layout(self):  # Create the layout for the widgets
        # Configure grid for the info frame
        self.info_frame.columnconfigure(0, weight=1, minsize=540)
        self.info_frame.rowconfigure((0, 1, 2, 3, 4), weight=1)

        # Layout for NPC attributes
        self.health_label.grid(row=0, column=0, sticky="w", padx=20, pady=5)
        self.name_label.grid(row=1, column=0, sticky="w", padx=20, pady=5)
        self.race_label.grid(row=2, column=0, sticky="w", padx=20, pady=5)
        self.class_label.grid(row=3, column=0, sticky="w", padx=20, pady=5)
        self.alignment_label.grid(row=4, column=0, sticky="w", padx=20, pady=5)

        # Layout for buttons
        self.gen_button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        # Layout for the textbox
        self.info_textbox.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

    def start_gen(self): # Start the generation process and thread the generation to avoid freezing the GUI
        self.default_labels()
        self.info_textbox.configure(state="normal")
        self.info_textbox.delete("1.0", "end")
        self.info_textbox.insert("1.0", "Generating NPC info...")
        self.info_textbox.configure(state="disabled")
        self.gen_button.configure(state="disabled")
        generation_thread = Thread(target=self.generate)
        generation_thread.start()

    def generate(self):  # Generate each field for the NPC
        self.generator.generate_health()
        self.generator.generate_class()
        self.generator.generate_race()
        self.generator.generate_alignment()
        self.generator.generate_name()
        self.generator.generate_description()
        self.info_textbox.configure(state="normal")
        self.info_textbox.delete("1.0", "end")  # Clear the text box
        self.info_textbox.insert("1.0", (self.generator.description))
        self.info_textbox.configure(state="disabled")
        self.update_labels()
        self.gen_button.configure(state="normal")

    def update_labels(self):  # Update the labels with the generated values
        self.health_label.configure(
            text="Health Points: " + str(self.generator.healthPoints)
        )
        self.name_label.configure(text="Name: " + self.generator.name)
        self.race_label.configure(text="Race: " + self.generator.race)
        self.class_label.configure(text="Class: " + self.generator.class_)
        self.alignment_label.configure(text="Alignment: " + self.generator.alignment)

    def default_labels(self): # Reset the labels to default values
        self.health_label.configure(text="Health Points: ")
        self.name_label.configure(text="Name: ")
        self.race_label.configure(text="Race: ")
        self.class_label.configure(text="Class: ")
        self.alignment_label.configure(text="Alignment: ")
