import random
import numpy as np

from hub.bot import Bot


class RandomBot(Bot):
    def __init__(self):
        pass
    

    def set_state(self, state : dict) -> dict:
        field = [[0 for _ in range(10)] for _ in range(10)]
        ship_number = 1

        for ship_length in range(4, 0, -1):
            for _ in range(5 - ship_length):
                while True:
                    x, y = random.randint(0, 9), random.randint(0, 9)
                    direction = random.choice(['horizontal', 'vertical'])
                    if direction == 'horizontal' and x + ship_length > 9:
                        continue
                    if direction == 'vertical' and y + ship_length > 9:
                        continue
                    if any(field[y + i if direction == 'vertical' else y][x + i if direction == 'horizontal' else x] == 1 for i in range(ship_length)):
                        continue

                    for i in range(ship_length):
                        field[y + i if direction == 'vertical' else y][x + i if direction == 'horizontal' else x] = ship_number
                    ship_number += 1
                    break

        return { 'field' : field }

    

    def make_action(self, state : dict) -> dict:
        array = np.array(state['field'])
        zero_coordinates = np.argwhere(array == 0)
        random_zero = zero_coordinates[np.random.choice(zero_coordinates.shape[0])]
        
        return {'x' : random_zero[0], 'y' : random_zero[1]}
    