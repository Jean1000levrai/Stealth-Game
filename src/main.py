import easyPyEngine.easyPyEngine as epe
from player import Player
from var import *
import mob
import random
from platform import Platform

def generate_platforms(engine, count=5):
    platforms = []
    for _ in range(count):
        x = random.randint(0, 650)  # Keep inside screen width
        y = random.randint(200, 400)  # Random height in air
        platforms.append(Platform(engine, x, y))
    return platforms

def update(dt: float) -> None:
    engine.clear((0,181,226))

    engine.draw_rect(0, 500, 800, 600, (124, 252, 0), 1)

    # Draw platforms
    for platform in platforms:
        platform.draw()
    
    # update mobs first for collisions
    for mob in mobs:
        mob.update_mob(dt)
        mob.draw_mob()
        
    player.update_player(dt, mobs, platforms)
    player.draw_player()

if __name__ == "__main__":
    engine = epe.Engine("My Game", 800, 600)

    platforms = generate_platforms(engine, 2)
    mobs = [mob.Mob(engine, random.randint(0, 700), 450) for _ in range(3)]
    player = Player(engine, 100, 400)





    engine.run(update)
    engine.quit()