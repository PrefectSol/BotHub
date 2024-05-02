import random
import numpy as np

from hub.bot import Bot


class RandomBot(Bot):
    def __init__(self):
        pass
    

    def set_state(self, state : dict = None) -> dict:
        field = [[0 for _ in range(10)] for _ in range(10)]
        ship_counter = 1
        ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        
        for ship in ships:
            while True:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                direction = random.choice(("h", "v"))
                if direction == "h" and x + ship > 10:
                    continue
                elif direction == "v" and y + ship > 10:
                    continue
                if direction == "h":
                    if any(field[y][_x] != 0 for _x in range(x, x + ship)):
                        continue
                    for _x in range(max(x-1, 0), min(x + ship + 1, 10)):
                        for _y in range(max(y-1, 0), min(y + 2, 10)):
                            if field[_y][_x] != 0:
                                break
                        else:
                            continue
                        break
                    else:
                        for _x in range(x, x + ship):
                            field[y][_x] = ship_counter
                        break
                else:
                    if any(field[_y][x] != 0 for _y in range(y, y + ship)):
                        continue
                    for _x in range(max(x-1, 0), min(x + 2, 10)):
                        for _y in range(max(y-1, 0), min(y + ship + 1, 10)):
                            if field[_y][_x] != 0:
                                break
                        else:
                            continue
                        break
                    else:
                        for _y in range(y, y + ship):
                            field[_y][x] = ship_counter
                        break
            ship_counter += 1

        return { 'field' : field }
    

    def make_action(self, state : dict) -> dict:
        array = np.array(state)
        zero_coordinates = np.argwhere(array == 0)
        random_zero = zero_coordinates[np.random.choice(zero_coordinates.shape[0])]

        return {'x' : random_zero[0], 'y' : random_zero[1]}