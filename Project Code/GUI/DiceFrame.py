import customtkinter as ctk
import random

class DiceRoller(ctk.CTkFrame):
    def __init__(self, master):  # Initializer
        super().__init__(master)

        self.create_widgets()
        self.create_layout()
    
    def create_widgets(self):
        # Create a text box to display roll results
        self.result_box = ctk.CTkTextbox(self, width=300, height=200, font=("Arial", 18))
        self.result_box.configure(state="disabled")  # Make it read-only initially

        # Create an entry box for the user to input the number of sides
        self.entry = ctk.CTkEntry(self, placeholder_text="Enter dice sides and amount (e.g., 2d6)")

        # Bind the Enter key to the roll_dice function
        self.entry.bind("<Return>", self.handle_roll)

        for i in range(23):
            self.result_box.configure(state="normal")  # Enable editing
            self.result_box.insert("end", "" + "\n")  # Append the text at the bottom
            self.result_box.configure(state="disabled")  # Make it read-only again
            self.result_box.see("end")

    def create_layout(self):
    # Configure the grid layout
        self.grid_rowconfigure(0, weight=1)  # Make the text box row expandable
        self.grid_rowconfigure(1, weight=0)  # Keep the entry box row fixed
        self.grid_columnconfigure(0, weight=1)  # Make the column expandable

    # Layout for the text box (takes up most of the frame)
        self.result_box.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # Fill the space

    # Layout for the entry box (at the bottom)
        self.entry.grid(row=1, column=0, padx=10, pady=10, sticky="ew")  # Stretch horizontally

    def handle_roll(self, event):
        """Handle the Enter key press to roll the dice."""
        try:
            # Parse the input (e.g., "2d4")
            input_text = self.entry.get().lower().strip()
            if "d" in input_text:
                num, sides = map(int, input_text.split("d"))  # Split into number of dice and sides
                if num > 0 and sides > 0:
                    self.roll_dice(sides, num)
                else:
                    self.append_to_result_box("Invalid: Enter positive numbers (e.g., 2d4)")
            else:
                self.append_to_result_box("Invalid: Use format 'NdX' (e.g., 2d4)")
        except ValueError:
            self.append_to_result_box("Invalid: Enter a valid number")

    def roll_dice(self, sides, num):
        """Roll the dice and update the result box."""
        self.entry.delete(0, "end")  # Clear the entry box
        result = 0
        rolls = []  # To store individual roll results
        for i in range(num):
            roll = random.randint(1, sides)  # Roll the dice
            rolls.append(roll)
            result += roll
        # Append the result to the text box
        self.append_to_result_box(f"Rolled {num}d{sides}: {result} (Rolls: {', '.join(map(str, rolls))})")

    def append_to_result_box(self, text):
        self.result_box.configure(state="normal")  # Enable editing
        self.result_box.insert("end", text + "\n")  # Append the text at the bottom
        self.result_box.configure(state="disabled")  # Make it read-only again
        self.result_box.see("end")  # Automatically scroll to the bottom