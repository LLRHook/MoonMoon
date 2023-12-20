import tkinter as tk
import random

class GameApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=400, height=300)
        self.canvas.pack()

        self.player = self.canvas.create_rectangle(50, 50, 100, 100, fill="blue")
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

    def move_player(self, event):
        if event.keysym == 'Up':
            self.canvas.move(self.player, 0, -10)
        elif event.keysym == 'Down':
            self.canvas.move(self.player, 0, 10)
        elif event.keysym == 'Left':
            self.canvas.move(self.player, -10, 0)
        elif event.keysym == 'Right':
            self.canvas.move(self.player, 10, 0)

    def spawn_enemy(self):
        x1 = random.randint(50, 350)
        y1 = random.randint(50, 250)
        enemy = self.canvas.create_rectangle(x1, y1, x1+50, y1+50, fill="red")
        self.enemies.append(enemy)
        self.root.after(2000, self.spawn_enemy)

    def shoot_bullet(self, event):
        x1, y1, x2, y2 = self.canvas.coords(self.player)
        bullet = self.canvas.create_oval(x1+20, y1-10, x2-20, y1, fill="yellow")
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
