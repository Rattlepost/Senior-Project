import customtkinter as ctk
import random


class DiceRoller(ctk.CTkFrame):
    def __init__(self, master):  # Initializer
        super().__init__(master)

        self.history = []  # List to store the history of entries for each session
        self.history_index = -1  # Index to track the current position in history
        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        # Create a text box to display roll results
        self.result_box = ctk.CTkTextbox(
            self, width=300, height=200, font=("Arial", 16)
        )
        self.result_box.configure(state="disabled")  # Make it read-only initially

        # Create an entry box for the user to input the number of sides
        self.entry = ctk.CTkEntry(
            self, placeholder_text="Enter dice sides and amount (e.g., 2d6)"
        )

        # Bind the Enter key to the roll_dice function
        self.entry.bind("<Return>", self.handle_roll)

        # Bind the Up Arrow key to navigate through history
        self.entry.bind("<Up>", self.fill_previous_entry)

    def create_layout(self):
        # Configure the grid layout
        self.grid_rowconfigure(0, weight=1)  # Make the text box row expandable
        self.grid_rowconfigure(1, weight=0)  # Keep the entry box row fixed
        self.grid_columnconfigure(0, weight=1)  # Make the column expandable

        # Layout for the text box (takes up most of the frame)
        self.result_box.grid(
            row=0, column=0, padx=10, pady=10, sticky="nsew"
        )  # Fill the space

        # Layout for the entry box (at the bottom)
        self.entry.grid(
            row=1, column=0, padx=10, pady=10, sticky="ew"
        )  # Stretch horizontally

    def handle_roll(self, event):
        try:
            # Parse the input (e.g., "2d4")
            input_text = self.entry.get().lower().strip()
            if "d" in input_text:
                num, sides = map(
                    int, input_text.split("d")
                )  # Split into number of dice and sides
                if num > 0 and sides > 0:
                    self.roll_dice(sides, num)
                    self.history.append(input_text)  # Save the input to history
                    self.history_index = len(self.history)  # Reset the history index
                else:
                    self.send_to_result_box(
                        "Invalid: Enter positive numbers (e.g., 2d4)"
                    )
            elif "" in input_text:
                return
            else:
                self.send_to_result_box("Invalid: Use format 'NdX' (e.g., 2d4)")
        except ValueError:
            self.send_to_result_box("Invalid: Enter a valid number")

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
        self.send_to_result_box(
            f"Rolled {num}d{sides}: {result} (Rolls: {', '.join(map(str, rolls))})"
        )

    def send_to_result_box(self, text):
        """Append text to the result box."""
        self.result_box.configure(state="normal")  
        self.result_box.insert("end", text + "\n")  
        self.result_box.configure(state="disabled") 
        self.result_box.see("end")  # Automatically scroll to the bottom

    def fill_previous_entry(self, event):
        if self.history and self.history_index > 0:
            self.history_index -= 1  # Move to the previous entry
            self.entry.delete(0, "end")  # Clear the current entry
            self.entry.insert(
                0, self.history[self.history_index]
            )  # Fill with the previous entry
