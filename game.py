import random
from constants import *

def spawn_new_tile(board):
    """Thêm ô số mới."""
    empty_tiles = [(r, c) for r in range(SIZE) for c in range(SIZE) if board[r][c] == 0]
    if empty_tiles:
        r, c = random.choice(empty_tiles)
        board[r][c] = 2 if random.random() < 0.9 else 4

def slide_row_left(row):
    """Trượt hàng sang trái và tính điểm."""
    new_row = [i for i in row if i != 0]  # Loại bỏ các ô 0
    score = 0
    for i in range(len(new_row) - 1):
        # Kiểm tra nếu hai ô số giống nhau thì gộp lại
        if new_row[i] == new_row[i + 1]:
            new_row[i] *= 2
            score += new_row[i]
            new_row[i + 1] = 0  # Đặt ô số sau thành 0 sau khi gộp
    new_row = [i for i in new_row if i != 0]  # Loại bỏ ô 0 sau khi gộp
    return new_row + [0] * (SIZE - len(new_row)), score  # Đảm bảo kích thước hàng đúng

def slide_left(board):
    """Trượt toàn bộ bàn cờ sang trái."""
    new_board = []
    total_score = 0
    for row in board:
        new_row, score = slide_row_left(row)
        new_board.append(new_row)
        total_score += score
    return new_board, total_score

def rotate_board(board):
    """Xoay bàn cờ 90 độ (trái kim đồng hồ)."""
    return [list(row) for row in zip(*board[::-1])]

def move(board, direction):
    """Di chuyển bàn cờ theo hướng."""
    for _ in range(direction):
        board = rotate_board(board)  # Xoay bàn cờ theo hướng
    board, score = slide_left(board)  # Di chuyển sang trái
    for _ in range(-direction % 4):  # Xoay lại về hướng ban đầu
        board = rotate_board(board)
    return board, score

def is_game_over(board):
    """Kiểm tra xem trò chơi có kết thúc hay không."""
    # Kiểm tra tất cả các hàng và cột để xem còn di chuyển được không
    for row in board:
        for i in range(SIZE - 1):
            if row[i] == row[i + 1] or row[i] == 0:  # Có thể trượt hoặc ghép
                return False
    for col in zip(*board):
        for i in range(SIZE - 1):
            if col[i] == col[i + 1] or col[i] == 0:  # Có thể trượt hoặc ghép
                return False
    return True  # Không còn di chuyển được nữa

def get_rank(score):
    """Xác định hạng dựa trên điểm số."""
    if score < 500:
        return "Beginner"
    elif score < 2000:
        return "Intermediate"
    elif score < 5000:
        return "Advanced"
    else:
        return "Master"
