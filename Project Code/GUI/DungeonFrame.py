import customtkinter as ctk
import dungeonGen as dg
from openai import OpenAI
from threading import Thread
import os
from dotenv import load_dotenv

class DungeonFrame(ctk.CTkFrame):
    def __init__(self, master, num_rooms):  # Initializer
        super().__init__(master)
        self.num_rooms = num_rooms  # Store the number of rooms

        # Load environment variables from .env file
        load_dotenv()

        # Retrieve the OpenAI API key from the .env file
        api_key = os.getenv("OPENAI_API_KEY")

        # Initialize the OpenAI client with the API key
        self.client = OpenAI(api_key=api_key)

        self.canvas = ctk.CTkCanvas(self, width=400, height=400, bg="black")
        self.canvas.pack(pady=20)
        self.create_widgets()
        self.create_layout()

    def create_widgets(self):  # Create buttons and labels
        self.room_field = ctk.CTkSlider(self, from_=5, to=25, orientation='horizontal', state='normal', number_of_steps=25, command=self.update_label)
        self.room_field.set(self.num_rooms)
        self.room_label = ctk.CTkLabel(self, text=f'Number of Rooms: {self.num_rooms}')
        self.generate_button = ctk.CTkButton(self, text='Generate Dungeon', command=self.start_generation)

        # Add a text box to display room descriptions
        self.description_box = ctk.CTkTextbox(self, width=400, height=200)

        # Add a button to pop out the description box
        self.popout_button = ctk.CTkButton(self, text="Pop Out Descriptions", command=self.popout_description_box)

    def create_layout(self):  # Create the layout for the widgets
        self.room_field.pack(pady=10)
        self.room_label.pack(pady=2)
        self.generate_button.pack(pady=2)
        self.popout_button.pack(pady=2)
        self.description_box.pack(pady=2)
        
    def start_generation(self):  # Start dungeon generation with loading animation
        # Run dungeon generation in a separate thread
        self.generate_button.configure(state="disabled")
        self.popout_button.configure(state="disabled")
        generation_thread = Thread(target=self.regenerate_dungeon)
        generation_thread.start()
        self.description_box.delete("1.0", "end")  # Clear the text box
        self.description_box.insert("1.0", "Generating room descriptions...")
        
    def update_label(self, value):  # Update the label when the slider is moved
        self.num_rooms = int(value)
        self.room_label.configure(text=f'Number of Rooms: {self.num_rooms}')

    def draw_dungeon(self, dungeon):  # Draw the dungeon on the canvas
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

        self.generate_room_descriptions(dungeon)  # Generate room descriptions using AI

    def regenerate_dungeon(self):  # Regenerate the dungeon when the button is pressed
        self.draw_dungeon(dg.generate_dungeon(self.num_rooms))
        self.generate_button.configure(state="normal")
        self.popout_button.configure(state="normal")
    
    def generate_room_descriptions(self, dungeon):  # Generate room descriptions using AI
        descriptions = []
        for room in dungeon:
            prompt = f"Simply and shortly describe a dungeon room with the following specifications:\n" \
                    f"Shape: {room.shape}\n" \
                    f"Number of connections: {len(room.connections)}\n" \
                    f"A number of traps between 0 and 3\n" \
                    f"A number of monsters between 0 and 4\n" \
                    f"A number of treasures between 0 and 2\n" \
                    f"The traps, monsters, and treasure amounts in a room should not exceed 5 added together\n" \
                    f"A room with monsters should not have traps\n" \
                       

            try:
                response = self.client.chat.completions.create(
                    model="gpt-4o",
                    messages= [
                        {"role": "user", "content": prompt}
                    ],
                )
                description = response.choices[0].message.content.strip()
                descriptions.append(f"Room {room.room_id}: {description}")
            except Exception as e:
                descriptions.append(f"Room {room.room_id}: Failed to generate description. Error: {e}")

        # Display the descriptions in the text box
        self.description_box.delete("1.0", "end")  # Clear the text box
        self.description_box.insert("1.0", "\n\n".join(descriptions))  # Add the descriptions

    def popout_description_box(self):  # Pop out the description box into a new window
        popout_window = ctk.CTkToplevel()  # Create a new Toplevel window
        popout_window.title("Room Descriptions")
        popout_window.geometry("700x400")
        popout_window.attributes("-topmost", True)  # Keep the popout window on top


        # Add a label to the popout window
        popout_label = ctk.CTkLabel(popout_window, text="Room Descriptions")
        popout_label.pack(pady=10)

        # Add a textbox to the popout window
        popout_textbox = ctk.CTkTextbox(popout_window, wrap="word", font=("Arial", 14))
        popout_textbox.pack(pady=10, padx=10, fill="both", expand=True)

        # Copy the content from the main description box to the popout textbox
        content = self.description_box.get("1.0", "end-1c")
        popout_textbox.insert("1.0", content)

        # Make the popout textbox read-only
        popout_textbox.configure(state="disabled")