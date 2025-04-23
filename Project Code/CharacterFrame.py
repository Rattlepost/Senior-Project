import customtkinter as ctk
import random


class CharacterFrame(ctk.CTkFrame):
    def __init__(self, master, npc_data, save_callback):  # Initializer
        super().__init__(master)

        self.npc_data = npc_data  # Store NPC data
        self.save_callback = save_callback  # Callback to save data
        self.configure(fg_color="#3E3E3E")  # Dark grey hex color
        roll = 0  # Placeholder for roll value
        self.create_widgets()
        self.create_layout()

    def create_widgets(self):  # Create buttons and labels
        self.delete_button = ctk.CTkButton(
            self, text="Delete", command=self.delete_npc, width=50
        )

        self.roll_button = ctk.CTkButton(
            self, text="Roll d20", command=self.roll, width=50
        )
        self.roll_label = ctk.CTkLabel(self, text="Roll: -", font=("Arial", 20))

        self.name_label = ctk.CTkLabel(self, text="Name:")
        self.name_entry = ctk.CTkEntry(self, width=150)
        self.name_entry.insert(
            0, self.npc_data["name"]
        )  # grabs the saved name from the npc_data.json file,
        #   and repeats for the rest of the entries
        self.health_label = ctk.CTkLabel(self, text="HP:")
        self.health_entry = ctk.CTkEntry(self, width=50)
        self.health_entry.insert(0, str(self.npc_data["health"]))

        self.ac_label = ctk.CTkLabel(self, text="AC:")
        self.ac_entry = ctk.CTkEntry(self, width=50)
        self.ac_entry.insert(0, str(self.npc_data["ac"]))

        self.prof_label = ctk.CTkLabel(self, text="Prof:")
        self.prof_entry = ctk.CTkEntry(self, width=50)
        self.prof_entry.insert(0, str(self.npc_data["prof"]))

        self.str_label = ctk.CTkLabel(self, text="Str:")
        self.str_entry = ctk.CTkEntry(self, width=50)
        self.str_entry.insert(0, str(self.npc_data["str"]))

        self.dex_label = ctk.CTkLabel(self, text="Dex:")
        self.dex_entry = ctk.CTkEntry(self, width=50)
        self.dex_entry.insert(0, str(self.npc_data["dex"]))

        self.con_label = ctk.CTkLabel(self, text="Con:")
        self.con_entry = ctk.CTkEntry(self, width=50)
        self.con_entry.insert(0, str(self.npc_data["con"]))

        self.int_label = ctk.CTkLabel(self, text="Int:")
        self.int_entry = ctk.CTkEntry(self, width=50)
        self.int_entry.insert(0, str(self.npc_data["int"]))

        self.wis_label = ctk.CTkLabel(self, text="Wis:")
        self.wis_entry = ctk.CTkEntry(self, width=50)
        self.wis_entry.insert(0, str(self.npc_data["wis"]))

        self.cha_label = ctk.CTkLabel(self, text="Cha:")
        self.cha_entry = ctk.CTkEntry(self, width=50)
        self.cha_entry.insert(0, str(self.npc_data["cha"]))

    def create_layout(self):  # Create layout for the widgets in a grid format

        self.delete_button.grid(
            row=0, column=5, columnspan=2, padx=3, pady=5, sticky="e"
        )

        self.roll_button.grid(
            row=0, column=7, columnspan=2, padx=10, pady=5, sticky="e"
        )
        self.roll_label.grid(
            row=1, column=7, columnspan=2, rowspan=3, padx=10, pady=5, sticky="e"
        )

        self.name_label.grid(row=0, column=0, padx=3, pady=5, sticky="w")
        self.name_entry.grid(row=0, column=1, columnspan=3, padx=3, pady=5, sticky="w")

        self.str_label.grid(row=1, column=0, padx=3, sticky="w")
        self.str_entry.grid(row=1, column=1, padx=3, sticky="w")

        self.int_label.grid(row=1, column=2, padx=3, sticky="w")
        self.int_entry.grid(row=1, column=3, padx=3, sticky="w")

        self.health_label.grid(row=1, column=4, padx=3, sticky="w")
        self.health_entry.grid(row=1, column=5, padx=3, sticky="w")

        self.prof_label.grid(row=3, column=4, padx=8, sticky="w")
        self.prof_entry.grid(row=3, column=5, padx=3, sticky="w")

        self.dex_label.grid(row=2, column=0, padx=3, sticky="w")
        self.dex_entry.grid(row=2, column=1, padx=3, sticky="w")

        self.wis_label.grid(row=2, column=2, padx=3, sticky="w")
        self.wis_entry.grid(row=2, column=3, padx=3, sticky="w")

        self.ac_label.grid(row=2, column=4, padx=3, sticky="w")
        self.ac_entry.grid(row=2, column=5, padx=3, sticky="w")

        self.con_label.grid(row=3, column=0, padx=3, sticky="w")
        self.con_entry.grid(row=3, column=1, padx=3, sticky="w")

        self.cha_label.grid(row=3, column=2, padx=3, sticky="w")
        self.cha_entry.grid(row=3, column=3, padx=3, sticky="w")

    def get_npc_data(self):  # Gets the data for the specified entry
        return {
            "name": self.name_entry.get(),
            "health": (self.health_entry.get()),
            "ac": (self.ac_entry.get()),
            "prof": (self.prof_entry.get()),
            "str": (self.str_entry.get()),
            "dex": (self.dex_entry.get()),
            "con": (self.con_entry.get()),
            "int": (self.int_entry.get()),
            "wis": (self.wis_entry.get()),
            "cha": (self.cha_entry.get()),
        }

    def delete_npc(self):  # Deletes the current NPC and saves the updated data
        self.save_callback()  # Save updated data
        self.destroy()

    def roll(self):  # Rolls a d20 and updates the label with the result
        roll = random.randint(1, 20)
        self.roll_label.configure(text="Roll: " + str(roll))
