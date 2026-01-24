import easyPyEngine.easyPyEngine as epe
import player
from var import *
import mob
import random



def update(dt: float) -> None:
    engine.clear((0,181,226))

    engine.draw_rect(0, 500, 800, 600, (124, 252, 0), 1)
    
    # update mobs first for collisions
    for mob in mobs:
        mob.update_mob(dt)
        mob.draw_mob()
        
    player.update_player(dt, mobs)
    player.draw_player()

if __name__ == "__main__":
    engine = epe.Engine("My Game", 800, 600)


    mobs = [mob.Mob(engine, random.randint(0, 700), 450) for _ in range(3)]
    player = player.Player(engine, 100, 400)





    engine.run(update)
    engine.quit()