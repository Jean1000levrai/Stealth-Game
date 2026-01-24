import random

class Platform:
    def __init__(self, engine, x, y, width=150, height=20, color=(139, 69, 19)):
        self.engine = engine
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        self.engine.draw_rect(self.x, self.y, self.width, self.height, self.color, 1)

    def collides_with_player(self, player):
        # Check if player is at same y range and pressing E
        return (
            player.y >= self.y and
            player.y <= self.y + self.width and
            player.engine.is_key_pressed("e")
        )
