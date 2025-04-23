import random


class Room:
    def __init__(self, room_id, position, shape):  # Initializer
        self.room_id = room_id  # Unique identifier for the room
        self.position = position  # Position of the room in the dungeon
        self.shape = shape  # Shape of the room (e.g., square, circle)
        self.connections = []

    def add_connection(self, connection):  # Add a connection to another room
        self.connections.append(connection)
        connection.connections.append(self)

    def __repr__(self):  # String representation of the room for debugging
        return f"Room {self.room_id} at {self.position} shaped {self.shape} connected to {[room.room_id for room in self.connections]}"


def generate_dungeon(
    num_rooms,
):  # Function to generate a dungeon with a given number of rooms
    if num_rooms < 1:  # Check if the number of rooms is valid
        return []

    dungeon = []
    start_room = Room(1, (0, 0), "square")
    dungeon.append(start_room)
    room_positions = {(0, 0)}

    for room_id in range(2, num_rooms + 1):  # Loop to create rooms
        while True:
            parent_room = random.choice(dungeon)
            x, y = parent_room.position
            direction = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
            new_position = (x + direction[0], y + direction[1])
            if (
                -3 < new_position[0] < 3 and -3 < new_position[1] < 3
            ):  # Check if the new position is within bounds of canvas
                if new_position not in room_positions:
                    new_shape = random.choice(["square", "circle"])
                    new_room = Room(room_id, new_position, new_shape)
                    parent_room.add_connection(new_room)
                    dungeon.append(new_room)
                    room_positions.add(new_position)
                    break

    return dungeon
