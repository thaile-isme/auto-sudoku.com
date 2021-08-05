import pynput
from time import sleep

mouse = pynput.mouse.Controller()
sleep(3)
'''
Run this file, move your cursor to the position you need to know
Then wait for 3 seconds
'''
print(mouse.position)
