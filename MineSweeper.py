import tkinter as tk
import random

global total
total = 0


class Minesweeper:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("MineSweeper")
        self.frame = tk.Frame(self.root, width=450, height=50, pady=3)
        self.frame.pack(expand=1)
        self.board()
        self.root.mainloop()

    def board(self):
        global val
        # tk = Tk()
        self.button11 = tk.Button(self.frame, height=2, width=4, command=lambda: self.game(self.button11))
        self.button12 = tk.Button(self.frame, height=2, width=4, command=lambda: self.game(self.button12))
        self.button13 = tk.Button(self.frame, height=2, width=4, command=lambda: self.game(self.button13))
        self.button14 = tk.Button(self.frame, height=2, width=4, command=lambda: self.game(self.button14))
        self.button15 = tk.Button(self.frame, height=2, width=4, command=lambda: self.game(self.button15))
        self.button21 = tk.Button(self.frame, height=2, width=4, command=lambda: self.game(self.button21))
        self.button22 = tk.Button(self.frame, height=2, width=4, command=lambda: self.game(self.button22))
        self.button23 = tk.Button(self.frame, height=2, width=4, command=lambda: self.game(self.button23))
        self.button24 = tk.Button(self.frame, height=2, width=4, command=lambda: self.game(self.button24))
        self.button25 = tk.Button(self.frame, height=2, width=4, command=lambda: self.game(self.button25))
        self.button31 = tk.Button(self.frame, height=2, width=4, command=lambda: self.game(self.button31))
        self.button32 = tk.Button(self.frame, height=2, width=4, command=lambda: self.game(self.button32))
        self.button33 = tk.Button(self.frame, height=2, width=4, command=lambda: self.game(self.button33))
        self.button34 = tk.Button(self.frame, height=2, width=4, command=lambda: self.game(self.button34))
        self.button35 = tk.Button(self.frame, height=2, width=4, command=lambda: self.game(self.button35))
        self.button41 = tk.Button(self.frame, height=2, width=4, command=lambda: self.game(self.button41))
        self.button42 = tk.Button(self.frame, height=2, width=4, command=lambda: self.game(self.button42))
        self.button43 = tk.Button(self.frame, height=2, width=4, command=lambda: self.game(self.button43))
        self.button44 = tk.Button(self.frame, height=2, width=4, command=lambda: self.game(self.button44))
        self.button45 = tk.Button(self.frame, height=2, width=4, command=lambda: self.game(self.button45))
        self.button51 = tk.Button(self.frame, height=2, width=4, command=lambda: self.game(self.button51))
        self.button52 = tk.Button(self.frame, height=2, width=4, command=lambda: self.game(self.button52))
        self.button53 = tk.Button(self.frame, height=2, width=4, command=lambda: self.game(self.button53))
        self.button54 = tk.Button(self.frame, height=2, width=4, command=lambda: self.game(self.button54))
        self.button55 = tk.Button(self.frame, height=2, width=4, command=lambda: self.game(self.button55))

        self.button11.grid(row=1, column=1)
        self.button12.grid(row=1, column=2)
        self.button13.grid(row=1, column=3)
        self.button14.grid(row=1, column=4)
        self.button15.grid(row=1, column=5)
        self.button21.grid(row=2, column=1)
        self.button22.grid(row=2, column=2)
        self.button23.grid(row=2, column=3)
        self.button24.grid(row=2, column=4)
        self.button25.grid(row=2, column=5)
        self.button31.grid(row=3, column=1)
        self.button32.grid(row=3, column=2)
        self.button33.grid(row=3, column=3)
        self.button34.grid(row=3, column=4)
        self.button35.grid(row=3, column=5)
        self.button41.grid(row=4, column=1)
        self.button42.grid(row=4, column=2)
        self.button43.grid(row=4, column=3)
        self.button44.grid(row=4, column=4)
        self.button45.grid(row=4, column=5)
        self.button51.grid(row=5, column=1)
        self.button52.grid(row=5, column=2)
        self.button53.grid(row=5, column=3)
        self.button54.grid(row=5, column=4)
        self.button55.grid(row=5, column=5)

        bomb_exist = True

        self.button_list = [self.button11, self.button12, self.button13, self.button14, self.button15,
                       self.button21, self.button22, self.button23, self.button24, self.button25,
                       self.button31, self.button32, self.button33, self.button34, self.button35,
                       self.button41, self.button42, self.button43, self.button44, self.button45,
                       self.button51, self.button52, self.button53, self.button54, self.button55]

        random_value = self.mine_sweeper(
            [[random.randint(0, 4), random.randint(0, 4)], [random.randint(0, 4), random.randint(0, 4)]],
            5, 5)
        value_list = []

        for i in random_value:
            for j in i:
                value_list.append(j)

        print(value_list)

        val = {}
        for i in range(25):
            val[self.button_list[i]] = value_list[i]
        # print(self.bomb_num)

        self.button11.bind('<Button-2>', lambda event, b=self.button11: self.right_click(event, b))
        self.button12.bind('<Button-2>', lambda event, b=self.button12: self.right_click(event, b))
        self.button13.bind('<Button-2>', lambda event, b=self.button13: self.right_click(event, b))
        self.button14.bind('<Button-2>', lambda event, b=self.button14: self.right_click(event, b))
        self.button15.bind('<Button-2>', lambda event, b=self.button15: self.right_click(event, b))
        self.button21.bind('<Button-2>', lambda event, b=self.button21: self.right_click(event, b))
        self.button22.bind('<Button-2>', lambda event, b=self.button22: self.right_click(event, b))
        self.button23.bind('<Button-2>', lambda event, b=self.button23: self.right_click(event, b))
        self.button24.bind('<Button-2>', lambda event, b=self.button24: self.right_click(event, b))
        self.button25.bind('<Button-2>', lambda event, b=self.button25: self.right_click(event, b))
        self.button31.bind('<Button-2>', lambda event, b=self.button31: self.right_click(event, b))
        self.button32.bind('<Button-2>', lambda event, b=self.button32: self.right_click(event, b))
        self.button33.bind('<Button-2>', lambda event, b=self.button33: self.right_click(event, b))
        self.button34.bind('<Button-2>', lambda event, b=self.button34: self.right_click(event, b))
        self.button35.bind('<Button-2>', lambda event, b=self.button35: self.right_click(event, b))
        self.button41.bind('<Button-2>', lambda event, b=self.button41: self.right_click(event, b))
        self.button42.bind('<Button-2>', lambda event, b=self.button42: self.right_click(event, b))
        self.button43.bind('<Button-2>', lambda event, b=self.button43: self.right_click(event, b))
        self.button44.bind('<Button-2>', lambda event, b=self.button44: self.right_click(event, b))
        self.button45.bind('<Button-2>', lambda event, b=self.button45: self.right_click(event, b))
        self.button51.bind('<Button-2>', lambda event, b=self.button51: self.right_click(event, b))
        self.button52.bind('<Button-2>', lambda event, b=self.button52: self.right_click(event, b))
        self.button53.bind('<Button-2>', lambda event, b=self.button53: self.right_click(event, b))
        self.button54.bind('<Button-2>', lambda event, b=self.button54: self.right_click(event, b))
        self.button55.bind('<Button-2>', lambda event, b=self.button55: self.right_click(event, b))


    def game(self, b):
        if val[b] == -1:
            self.game_over()
        else:
            self.show_number(b, int(val[b]))

    def game_over(self):
        self.frame.destroy()
        label_GG = tk.Label(text='Game Over')
        label_GG.grid(row=2, column=1)

    def show_number(self, b, n):
        if n >= 0:
            b['state'] = 'disable'
            b['text'] = n
            self.game_win()

    def game_win(self):
        self.button_state = []
        for i in self.button_list:
            print(i['state'])
            self.button_state.append(i['state'])
        print(self.button_state)
        if "normal" in self.button_state:
            pass
        else:
            self.frame.destroy()
            label_GG = tk.Label(text='You Win')
            label_GG.grid(row=2, column=1)

    def right_click(self, event, b):
        # print(int(val[b]))
        if int(val[b]) is -1:
            b['state'] = 'disable'
            b['text'] = 'X'
            print(int(val[b]))
            self.game_win()
        else:
            print(int(val[b]))
            self.game_over()

    def mine_sweeper(self, bombs, num_rows, num_cols):
        field = [[0 for i in range(num_cols)] for j in range(num_rows)]
        for bomb_location in bombs:
            (bomb_row, bomb_col) = bomb_location
            field[bomb_row][bomb_col] = -1

            row_range = range(bomb_row - 1, bomb_row + 2)
            col_range = range(bomb_col - 1, bomb_col + 2)

            for i in row_range:
                current_i = i
                for j in col_range:
                    current_j = j
                    if 0 <= i < num_rows and 0 <= j < num_cols and field[i][j] != -1:
                        field[i][j] += 1

        return field


# print(mine_sweeper([[0, 0], [1, 2]], 3, 4))
if __name__ == "__main__":
    Minesweeper()
