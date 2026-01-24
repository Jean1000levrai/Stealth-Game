import easyPyEngine.easyPyEngine as epe
from var import *

class Player:
    def __init__(self, engine, x, y, speed=200):
        self.engine = engine
        self.x = x
        self.y = y
        self.speed = speed

        # Load all sprites
        self.sprites = {}
        for direction, frames in player_img.items():
            self.sprites[direction] = {}
            for key, path in frames.items():
                self.sprites[direction][key] = epe.Sprite(engine, path, 100, 100)

        self.direction = "right"
        self.frame_counter = 0
        self.frame_delay = 0.1  # seconds per frame
        self.moving = False
        self.attacking = False
        self.attack_duration = 0.3  # seconds
        self.attack_timer = 0

        # Player size for collision detection
        self.width = 100
        self.height = 100

    def update_player(self, dt, mobs):
        self.moving = False

        # Move left/right
        if self.engine.is_key_pressed("a"):
            self.x -= self.speed * dt
            self.direction = "left"
            self.moving = True
        if self.engine.is_key_pressed("d"):
            self.x += self.speed * dt
            self.direction = "right"
            self.moving = True

        # Attack input
        if self.engine.is_key_pressed("space") and not self.attacking:
            self.attacking = True
            self.attack_timer = 0

        # Update attack timer
        if self.attacking:
            self.attack_timer += dt
            if self.attack_timer >= self.attack_duration:
                self.attacking = False

        # Collision detection with mobs
        if self.attacking:
            for mob in mobs[:]:  # iterate on a copy
                if self._collides_with(mob):
                    mobs.remove(mob)  # kill mob

        # Advance walk animation frame if moving
        if self.moving:
            self.frame_counter += dt
        else:
            self.frame_counter = 0

    def draw_player(self):
        # Determine which sprite to draw
        if self.attacking:
            sprite_to_draw = self.sprites[self.direction]["atk"]
        elif self.moving:
            frames = ["walk1", "walk2", "walk3"]
            index = int(self.frame_counter / self.frame_delay) % len(frames)
            sprite_to_draw = self.sprites[self.direction][frames[index]]
        else:
            sprite_to_draw = self.sprites[self.direction]["idle"]

        sprite_to_draw.draw(self.engine, self.x, self.y)

    def _collides_with(self, mob):
        # Simple AABB collision
        return (
            self.x < mob.x + mob.width and
            self.x + self.width > mob.x and
            self.y < mob.y + mob.height and
            self.y + self.height > mob.y
        )
