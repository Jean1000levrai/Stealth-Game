import easyPyEngine.easyPyEngine as epe
import random

engine = epe.Engine("My Game", 800, 600)

mob_img = {
    "left": "../assets/left/mob.png",
    "right": "../assets/right/mob.png"
}


class Mob:
    def __init__(self, engine, x, y, speed=100):
        self.engine = engine
        self.x = x
        self.y = y
        self.speed = speed

        # Load sprites
        self.sprites = {
            "left": epe.Sprite(engine, mob_img["left"], 80, 80),
            "right": epe.Sprite(engine, mob_img["right"], 80, 80)
        }

        self.direction = random.choice(["left", "right"])
        self.change_timer = 0
        self.change_interval = random.uniform(1, 3)  # seconds before changing direction

    def update(self, dt):
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

    def draw(self):
        self.sprites[self.direction].draw(self.engine, self.x, self.y)


# Create some mobs
mobs = [Mob(engine, random.randint(0, 700), 450) for _ in range(3)]


def update(dt):
    engine.clear(color=(135, 206, 235))
    engine.draw_rect(0, 500, 800, 600, (124, 252, 0), 1)

    # Update and draw mobs
    for mob in mobs:
        mob.update(dt)
        mob.draw()


engine.run(update)
engine.quit()
