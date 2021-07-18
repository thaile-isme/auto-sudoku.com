import numpy as np
import cv2
from PIL import ImageGrab
from time import sleep
import pynput
from copy import deepcopy

import solver

def get_img():
    im2 = ImageGrab.grab(bbox=(335, 482, 1280, 1427))
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

    # cv2.imshow("original", img)
    for i in range(9):
        w, h = templates[i].shape[::-1]
        res = cv2.matchTemplate(img_gray, templates[i], method)
        loc = np.where(res >= thresh_hold)
        for pt in zip(*loc[::-1]):
            # cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
            board[(pt[1] + h) // 105][(pt[0] + w) // 105] = i + 1
    # cv2.imshow("after", img)
    return board

def get_cells_pos():
    cells_pos = []
    for col in range(9):
        cells_pos.append([])
        for row in range(9):
            cells_pos[col].append([200 + row * 50, 280 + col * 50])
    return cells_pos


if __name__ == '__main__':
    get_img()
    board = img2array()                         # -> chuyển hình sang mảng

    result = deepcopy(board)
    solver.solveSudoku(result)                  # -> giải

    mouse = pynput.mouse.Controller()
    keyboard = pynput.keyboard.Controller()

    cells_pos = get_cells_pos()                 #
    mouse.position = cells_pos[0][0]            #
    mouse.click(pynput.mouse.Button.left, 1)    # -> click qua tab game
    sleep(0.2)                                  #

    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                mouse.position = cells_pos[row][col]
                sleep(0.15)
                mouse.click(pynput.mouse.Button.left, 1)
                num = result[row][col]
                keyboard.press(str(num))
