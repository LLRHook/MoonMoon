import tkinter as tk
import math

def rotate_shape(shape, angle, center):
    new_coords = []
    for i in range(0, len(shape), 2):
        x, y = shape[i], shape[i + 1]
        new_x = (x - center[0]) * math.cos(angle) - (y - center[1]) * math.sin(angle) + center[0]
        new_y = (x - center[0]) * math.sin(angle) + (y - center[1]) * math.cos(angle) + center[1]
        new_coords.extend([new_x, new_y])
    return new_coords

def move_player(event):
    global player_coords, player_direction
    if event.keysym in ["Left", "Right", "Up", "Down"]:
        # Calculate the rotation angle
        direction_angle = {"Left": 90, "Right": -90, "Up": 0, "Down": 180}
        angle = direction_angle[event.keysym] - player_direction
        player_direction = direction_angle[event.keysym]

        # Rotate the player
        angle_rad = math.radians(angle)
        rotated_coords = rotate_shape(player_coords, angle_rad, (50, 75))
        canvas.coords(player, rotated_coords)

def expand_area(event):
    if event.keysym == "Left":
        new_width = canvas.winfo_width() + 10
        canvas.config(width=new_width)
        root.geometry(f"{new_width}x{canvas.winfo_height()}+{root.winfo_x()-10}+{root.winfo_y()}")
    elif event.keysym == "Right":
        new_width = canvas.winfo_width() + 10
        canvas.config(width=new_width)
        root.geometry(f"{new_width}x{canvas.winfo_height()}")
    elif event.keysym == "Up":
        new_height = canvas.winfo_height() + 10
        canvas.config(height=new_height)
        root.geometry(f"{canvas.winfo_width()}x{new_height}+{root.winfo_x()}+{root.winfo_y()-10}")
    elif event.keysym == "Down":
        new_height = canvas.winfo_height() + 10
        canvas.config(height=new_height)
        root.geometry(f"{canvas.winfo_width()}x{new_height}")


if __name__ == "__main__":
    root = tk.Tk()
    canvas = tk.Canvas(root, width=500, height=500)
    canvas.pack()

    player_coords = [45, 80, 50, 70, 55, 80]
    player_direction = 0
    player = canvas.create_polygon(player_coords, outline="black")

    canvas.bind_all("<KeyPress-Left>", move_player)
    canvas.bind_all("<KeyPress-Right>", move_player)
    canvas.bind_all("<KeyPress-Up>", move_player)
    canvas.bind_all("<KeyPress-Down>", move_player)

    root.mainloop()