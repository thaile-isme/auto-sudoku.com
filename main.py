import numpy as np
import cv2
from PIL import ImageGrab
from time import sleep
import pynput
from copy import deepcopy
import solver

x1, y1 = 275, 482
x2, y2 = 1220, 1427
center_first_cell = 165, 268


def get_img(x1, y1, x2, y2):
    im2 = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    im2.save("board.png")


def img2array():
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    templates = [cv2.imread(
        './templates/' + str(i + 1
                             ) + '.png', 0) for i in range(9)]
    img = cv2.imread("board.png")
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    method = cv2.TM_CCOEFF_NORMED
    thresh_hold = .9

    for i in range(9):
        w, h = templates[i].shape[::-1]
        res = cv2.matchTemplate(img_gray, templates[i], method)
        loc = np.where(res >= thresh_hold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
            board[(pt[1] + h) // 105][(pt[0] + w) // 105] = i + 1
    cv2.imwrite('after.png', img)
    return board


def get_cells_pos(center_first_cell, gap=52):
    cells_pos = []
    for col in range(9):
        cells_pos.append([])
        for row in range(9):
            cells_pos[col].append([center_first_cell[0] + row * gap,
                                   center_first_cell[1] + col * gap])
    return cells_pos


def main():
    # Get and solve board
    get_img(x1, y1, x2, y2)
    board = img2array()
    result = deepcopy(board)
    solver.solveSudoku(result)

    # Initialize mouse and keyboard
    mouse = pynput.mouse.Controller()
    keyboard = pynput.keyboard.Controller()

    # Get all blank cell positions
    cells_pos = get_cells_pos(center_first_cell)
    mouse.position = cells_pos[0][0]
    sleep(0.1)
    mouse.click(pynput.mouse.Button.left, 1)
    sleep(0.1)

    # Automation
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                mouse.position = cells_pos[row][col]
                sleep(0.27)
                mouse.click(pynput.mouse.Button.left, 1)
                num = result[row][col]
                keyboard.press(str(num))
                sleep(0.1)


if __name__ == '__main__':
    main()
