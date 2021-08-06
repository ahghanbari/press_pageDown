#!/usr/bin/python3

from pynput.keyboard import Key, Controller
from time import sleep
from sys import argv

def main():
    if len(argv) < 2:
        print('You should pass one arg, the period time.\nlike:\npython3 press_PageDown 3')
        return
    
    keyboard = Controller()
    period = float(argv[1])
    
    sleep(1.5) # when you run this in termial and go to pdf reader for read, will take a time, this is for that
    while True:
        sleep(period)
        keyboard.press(Key.page_down)
        keyboard.release(Key.page_down)

if __name__ == '__main__':
    main()
