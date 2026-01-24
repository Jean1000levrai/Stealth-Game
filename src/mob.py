import easyPyEngine.easyPyEngine as epe
from var import mob_img
import random


class Mob:
    def __init__(self, engine, x, y, speed=100):
        self.engine = engine
        self.x = x
        self.y = y
        self.speed = speed
        self.width = 80
        self.height = 80

        self.sprites = {
            "left": epe.Sprite(engine, mob_img["left"], self.width, self.height),
            "right": epe.Sprite(engine, mob_img["right"], self.width, self.height)
        }

        self.direction = random.choice(["left", "right"])
        self.change_timer = 0
        self.change_interval = random.uniform(1, 3)

    def update_mob(self, dt):
        # Move in current direction
        if self.direction == "left":
            self.x -= self.speed * dt
        else:
            self.x += self.speed * dt

        # Keep mob inside screen bounds
        if self.x < 0:
            self.x = 0
            self.direction = "right"
        elif self.x > 800 - 80:
            self.x = 800 - 80
            self.direction = "left"

        # Randomly change direction
        self.change_timer += dt
        if self.change_timer >= self.change_interval:
            self.direction = random.choice(["left", "right"])
            self.change_timer = 0
            self.change_interval = random.uniform(1, 3)

    def draw_mob(self):
        self.sprites[self.direction].draw(self.engine, self.x, self.y)

