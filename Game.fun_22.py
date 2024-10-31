import tkinter as tk
import random

# Define constants for the game
BOARD_WIDTH = 10
BOARD_HEIGHT = 20
BLOCK_SIZE = 30
COLORS = ['#00FFFF', '#FF00FF', '#FFFF00', '#00FF00', '#FF0000']

SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]],  # Z
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]],  # J
]

class Tetris:
    def __init__(self, master):
        self.master = master
        self.master.title("Tetris")
        self.canvas = tk.Canvas(master, width=BOARD_WIDTH * BLOCK_SIZE, height=BOARD_HEIGHT * BLOCK_SIZE)
        self.canvas.pack()
        self.board = [[0] * BOARD_WIDTH for _ in range(BOARD_HEIGHT)]
        self.current_piece = None
        self.next_piece = self.new_piece()
        self.score = 0
        self.game_over = False
        self.spawn_piece()
        self.master.bind("<Left>", self.move_left)
        self.master.bind("<Right>", self.move_right)
        self.master.bind("<Down>", self.move_down)
        self.master.bind("<Up>", self.rotate_piece)
        self.update()

    def new_piece(self):
        shape = random.choice(SHAPES)
        color = COLORS[SHAPES.index(shape) % len(COLORS)]
        return {'shape': shape, 'color': color, 'x': BOARD_WIDTH // 2 - len(shape[0]) // 2, 'y': 0}

    def spawn_piece(self):
        self.current_piece = self.next_piece
        self.next_piece = self.new_piece()
        if self.check_collision(self.current_piece['shape'], self.current_piece['x'], self.current_piece['y']):
            self.game_over = True

    def check_collision(self, shape, x, y):
        for i, row in enumerate(shape):
            for j, block in enumerate(row):
                if block:
                    if (x + j < 0 or x + j >= BOARD_WIDTH or
                            y + i >= BOARD_HEIGHT or
                            self.board[y + i][x + j]):
                        return True
        return False

    def merge_piece(self):
        shape = self.current_piece['shape']
        x, y = self.current_piece['x'], self.current_piece['y']
        for i, row in enumerate(shape):
            for j, block in enumerate(row):
                if block:
                    self.board[y + i][x + j] = 1
        self.clear_lines()

    def clear_lines(self):
        new_board = [row for row in self.board if any(block == 0 for block in row)]
        lines_cleared = BOARD_HEIGHT - len(new_board)
        new_board = [[0] * BOARD_WIDTH for _ in range(lines_cleared)] + new_board
        self.board = new_board
        self.score += lines_cleared

    def move_left(self, event):
        if not self.game_over:
            self.current_piece['x'] -= 1
            if self.check_collision(self.current_piece['shape'], self.current_piece['x'], self.current_piece['y']):
                self.current_piece['x'] += 1

    def move_right(self, event):
        if not self.game_over:
            self.current_piece['x'] += 1
            if self.check_collision(self.current_piece['shape'], self.current_piece['x'], self.current_piece['y']):
                self.current_piece['x'] -= 1

    def move_down(self, event):
        if not self.game_over:
            self.current_piece['y'] += 1
            if self.check_collision(self.current_piece['shape'], self.current_piece['x'], self.current_piece['y']):
                self.current_piece['y'] -= 1
                self.merge_piece()
                self.spawn_piece()

    def rotate_piece(self, event):
        if not self.game_over:
            self.current_piece['shape'] = [list(row) for row in zip(*self.current_piece['shape'][::-1])]
            if self.check_collision(self.current_piece['shape'], self.current_piece['x'], self.current_piece['y']):
                self.current_piece['shape'] = [list(row) for row in zip(*self.current_piece['shape'])][::-1]

    def draw_board(self):
        self.canvas.delete("all")
        for i, row in enumerate(self.board):
            for j, block in enumerate(row):
                if block:
                    self.canvas.create_rectangle(j * BLOCK_SIZE, i * BLOCK_SIZE,
                                                  (j + 1) * BLOCK_SIZE, (i + 1) * BLOCK_SIZE,
                                                  fill='gray', outline='black')
        if self.current_piece:
            shape = self.current_piece['shape']
            color = self.current_piece['color']
            x, y = self.current_piece['x'], self.current_piece['y']
            for i, row in enumerate(shape):
                for j, block in enumerate(row):
                    if block:
                        self.canvas.create_rectangle((x + j) * BLOCK_SIZE, (y + i) * BLOCK_SIZE,
                                                      (x + j + 1) * BLOCK_SIZE, (y + i + 1) * BLOCK_SIZE,
                                                      fill=color, outline='black')

    def update(self):
        if not self.game_over:
            self.draw_board()
            self.move_down(None)  # Move the piece down automatically
            self.master.after(500, self.update)
        else:
            self.canvas.create_text(BOARD_WIDTH * BLOCK_SIZE / 2, BOARD_HEIGHT * BLOCK_SIZE / 2,
                                    text="Game Over", fill="red", font=("Arial", 24))

def main():
    root = tk.Tk()
    game = Tetris(root)
    root.mainloop()

if __name__ == "__main__":
    main()
