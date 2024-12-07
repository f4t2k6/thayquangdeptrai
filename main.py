import pygame
import sys
from game import get_rank, spawn_new_tile, move, is_game_over
from ui import draw_board, show_game_over
from score import load_high_score, save_high_score
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("2048")

    board = [[0] * SIZE for _ in range(SIZE)]
    spawn_new_tile(board)
    spawn_new_tile(board)
    
    score = 0
    high_score = load_high_score()
    running = True

    while running:
        draw_board(screen, board, score, high_score)  # Vẽ lại bàn cờ và điểm số
        pygame.display.flip()  # Cập nhật màn hình để hiển thị

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT):
                    direction = {pygame.K_UP: 1, pygame.K_RIGHT: 2, pygame.K_DOWN: 3, pygame.K_LEFT: 0}[event.key]
                    new_board, gained_score = move(board, direction)
                    if new_board != board:
                        board = new_board
                        score += gained_score
                        if score > high_score:
                            high_score = score
                        spawn_new_tile(board)
                        if is_game_over(board):
                            print("Game Over!")
                            save_high_score(high_score)
                            rank = get_rank(score)
                            show_game_over(screen, score, rank)  # Hiển thị kết thúc trò chơi
                            pygame.display.flip()  # Cập nhật màn hình sau khi hiển thị game over
                            pygame.time.wait(3000)  # Hiển thị game over trong 3 giây
                            running = False  # Dừng trò chơi sau khi kết thúc

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
