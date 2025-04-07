import customtkinter as ctk
import dungeonGen as dg

class DungeonFrame(ctk.CTkFrame):
    def __init__(self, master, num_rooms): #Initializer
        super().__init__(master)
        self.num_rooms = num_rooms # Store the number of rooms

        self.canvas = ctk.CTkCanvas(self, width=400, height=400, bg="black")
        self.canvas.pack(pady=20)
        self.create_widgets()
        self.create_layout()

    def create_widgets(self): # Create buttons and labels
        self.room_field = ctk.CTkSlider(self, from_=5, to=25, orientation='horizontal', state='normal', number_of_steps=25, command=self.update_label)
        self.room_field.set(self.num_rooms)
        self.room_label = ctk.CTkLabel(self, text=f'Number of Rooms: {self.num_rooms}')
        self.generate_button = ctk.CTkButton(self, text='Generate Dungeon', command=self.regenerate_dungeon)

    def create_layout(self): # Create the layout for the widgets
        self.room_field.pack(pady=10)
        self.room_label.pack(pady=10)
        self.generate_button.pack(pady=10)

    def update_label(self, value):# Update the label when the slider is moved
        self.num_rooms = int(value)
        self.room_label.configure(text=f'Number of Rooms: {self.num_rooms}')

    def draw_dungeon(self, dungeon): # Draw the dungeon on the canvas
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

    def regenerate_dungeon(self): # Regenerate the dungeon when the button is pressed
        self.draw_dungeon(dg.generate_dungeon(self.num_rooms))