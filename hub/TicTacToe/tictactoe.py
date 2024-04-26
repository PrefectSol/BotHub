# import json
# import random
# import re

# from tkinter import *
# from hub.game import Game


# class TicTacToe(Game):
#     def __init__(self, settings):
#         self._players_count = 2
#         self._field_size = 3
#         self._pady = 5
#         self._is_playing = True
#         self._winner = ''
#         self._move_symb = ['X', 'O']
#         self._clients = []
        
#         with open(settings, 'r') as file:
#             self._config = json.load(file)
            
#         if self._config['first move'] == 1 or self._config['first move'] == 2:
#             self._move = self._config['first move'] - 1
#         else:
#             self._move = random.randint(0, 1)
                    
    
#     def add_client(self, client_info, bot_impl) -> bool:
#         if len(self._clients) < self.players_count:
#             match = re.search('class (\\w+)', bot_impl)
#             if not match:
#                 return False
            
#             exec(bot_impl)
#             bot = eval(match.group(1))
#             self._clients.append((client_info, bot()))
            
#             return True
        
#         return False
        
            
#     # def __init_window(self):
#     #     self._window = Tk()
#     #     self._clicked = IntVar(value=0)
#     #     self._window.geometry(self._config['window']['geometry'])
#     #     self._window.title(self._config['window']['title'])

#     #     self._field = [['' for _ in range(self._field_size)] for _ in range(self._field_size)]
#     #     self._buttons = []
#     #     self._labels = []

#     #     grid_frame = Frame(self._window)
#     #     grid_frame.pack(side=LEFT, fill=BOTH, expand=True)

#     #     for x in range(self._field_size):
#     #         row = []
#     #         for y in range(self._field_size):
#     #             cell = Button(grid_frame, text='', command=lambda x=x, y=y: self.__selected(x, y), state=DISABLED)
#     #             cell.grid(row=x, column=y, sticky="nsew")
#     #             row.append(cell)
                
#     #         self._buttons.append(row)

#     #     entry_frame = Frame(self._window)
#     #     entry_frame.pack(side=RIGHT, fill=Y)

#     #     for i in range(self._field_size):
#     #         label = Label(entry_frame, text='')
#     #         label.pack(pady=self._pady)  
                        
#     #         self._labels.append(label)

#     #     for i in range(self._field_size):
#     #         grid_frame.grid_columnconfigure(i, weight=1)
#     #         grid_frame.grid_rowconfigure(i, weight=1)

            
#     # def __selected(self, x, y):
#     #     if self._field[x][y] == '':
#     #         self._s_x = x
#     #         self._s_y = y        
#     #         self._clicked.set(1)
        
#     # def __button_ctl(self, state_):
#     #     for row in self._buttons:
#     #         for cell in row:
#     #             cell.configure(state=state_)
            
        
#     # def __check_winner(self):
#     #     for i in range(self._field_size):
#     #         if self._field[i][0] == self._field[i][1] == self._field[i][2] != '':
#     #             self._winner = self._field[i][0]
#     #             self._is_playing = False
#     #             return
            
#     #         if self._field[0][i] == self._field[1][i] == self._field[2][i] != '':
#     #             self._winner = self._field[0][i]
#     #             self._is_playing = False
#     #             return
            
#     #     if self._field[0][0] == self._field[1][1] == self._field[2][2] != '':
#     #         self._winner = self._field[0][0]
#     #         self._is_playing = False
#     #         return
        
#     #     if self._field[0][2] == self._field[1][1] == self._field[2][0] != '':
#     #         self._winner = self._field[0][2]
#     #         self._is_playing = False
#     #         return
        
#     #     if all(self._field[i][j] != '' for i in range(self._field_size) for j in range(self._field_size)):
#     #         self._winner = 'Draw'
#     #         self._is_playing = False
#     #         return
    
    
#     # def run(self):
#     #     self._window.mainloop()
    
    
#     # def exit(self):
#     #     self._window.destroy()
    
    
#     # def get_state(self, _) -> dict:
#     #     self.__check_winner()
#     #     return {'players' : [f'client_{client[2]}' for client in self._clients],
#     #             'move' : self._move,
#     #             'winner' : self._winner,
#     #             'field' : self._field }
    
    
#     # def view_state(self, state : dict):
#     #     self._labels[0].config(text=f"Players: {state['players']}")
#     #     self._labels[1].config(text=f"Move: {state['players'][state['move']]}")
#     #     self._labels[2].config(text=f"Winner: {state['winner']}")
#     #     self._field = state['field']
        
#     #     for x in range(self._field_size):
#     #         for y in range(self._field_size):
#     #             self._buttons[x][y]['text'] = state['field'][x][y]
                
                
#     # def get_target(self) -> list:
#     #     return self._clients[self._move]

    
#     # def get_action(self) -> dict:
#     #     self.__button_ctl(ACTIVE)
#     #     self._window.wait_variable(self._clicked)    
#     #     self.__button_ctl(DISABLED)

#     #     return { 'x' : self._s_x, 'y' : self._s_y }
        
    
#     # def make_action(self, action : dict):
#     #     x = action['x']
#     #     y = action['y']
        
#     #     self._buttons[x][y]['text'] = self._move_symb[self._move]
#     #     self._field[x][y] = self._move_symb[self._move]

#     #     self._move = (self._move + 1) % self._players_count