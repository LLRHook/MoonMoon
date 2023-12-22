import tkinter as tk
import random
import math

class GameApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=400, height=300)
        self.canvas.pack()

        self.player = self.canvas.create_polygon(75, 50, 50, 100, 100, 100, outline="black", fill="blue")
        self.player_angle = 0  # Initial angle of the player
        self.player_speed = 10  # Speed of the player

        self.enemies = []
        self.bullets = []

        self.setup_bindings()
        self.spawn_enemy()

    def setup_bindings(self):
        self.canvas.bind_all('<KeyPress-Up>', self.move_player)
        self.canvas.bind_all('<KeyPress-Down>', self.move_player)
        self.canvas.bind_all('<KeyPress-Left>', self.move_player)
        self.canvas.bind_all('<KeyPress-Right>', self.move_player)
        self.canvas.bind_all('<space>', self.shoot_bullet)

    def rotate_polygon(self, polygon, angle, px, py):
        coords = self.canvas.coords(polygon)
        new_coords = []
        for i in range(0, len(coords), 2):
            x, y = coords[i], coords[i + 1]
            new_x = ((x - px) * math.cos(angle)) - ((y - py) * math.sin(angle)) + px
            new_y = ((x - px) * math.sin(angle)) + ((y - py) * math.cos(angle)) + py
            new_coords.extend([new_x, new_y])
        self.canvas.coords(polygon, new_coords)

    def move_player(self, event):
        if event.keysym == 'Up':
            dx = self.player_speed * math.cos(math.radians(self.player_angle))
            dy = -self.player_speed * math.sin(math.radians(self.player_angle))
            self.canvas.move(self.player, dx, dy)
        elif event.keysym == 'Left':
            self.player_angle = (self.player_angle - 10) % 360
            self.rotate_player()
        elif event.keysym == 'Right':
            self.player_angle = (self.player_angle + 10) % 360
            self.rotate_player()

    def rotate_player(self):
        coords = self.canvas.coords(self.player)
        center_x = (coords[0] + coords[4]) / 2
        center_y = (coords[1] + coords[5]) / 2
        self.rotate_polygon(self.player, math.radians(-10), center_x, center_y)

    def spawn_enemy(self):
        x1 = random.randint(50, 350)
        y1 = random.randint(50, 250)
        enemy = self.canvas.create_rectangle(x1, y1, x1+50, y1+50, fill="red")
        self.enemies.append(enemy)
        self.root.after(2000, self.spawn_enemy)

    def shoot_bullet(self, event):
        coords = self.canvas.coords(self.player)
        tip_x = coords[0]
        tip_y = coords[1]
        bullet = self.canvas.create_oval(tip_x-5, tip_y-10, tip_x+5, tip_y, fill="yellow")
        self.bullets.append(bullet)
        self.move_bullet(bullet)

    def move_bullet(self, bullet):
        self.canvas.move(bullet, 0, -10)
        if self.canvas.coords(bullet)[1] > 0:
            self.root.after(100, lambda: self.move_bullet(bullet))
        else:
            self.canvas.delete(bullet)
            self.bullets.remove(bullet)

if __name__ == "__main__":
    root = tk.Tk()
    game_app = GameApp(root)
    root.mainloop()
