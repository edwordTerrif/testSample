import os
import pyautogui as pyg
import func_block_code as vega
from pynput import mouse, keyboard
import csv
import time
import random

######////--                                                                              --\\\\######
##//                                                                                              \\##
#/__                                                                                              __\#
#                        shortcut key function ready for your key press                              #
#                       if in the case localkey presed macro starting trigger                        #
#/__                                                                                              __\#
##//                                                                                              \\##
######////--                                                                              --\\\\######


def listener_shortcut_key():
    with keyboard.Listener(on_press="") as key:  # in on_press have simple if
        try:
            key.join()
        except:
            print('end listener function')


def p1_press():
    pass


def p2_press():
    pass


if __name__ == "__main__":
    # first record func excute time
    start = time.perf_counter()
    ###-------------------------------------------------------------###
    #-----------------------------------------------------------------#
    #                                                                 #
    #             execute listener_shortcut_key function              #
    #                                                                 #
    #-----------------------------------------------------------------#
    ###-------------------------------------------------------------###
    listener_shortcut_key()
    # last record func excute time
    finish = time.perf_counter()
    ###-------------------------------------------------------------###
    #-----------------------------------------------------------------#
    #                                                                 #
    # last function executeing time and start max macro function time #
    #                                                                 #
    #-----------------------------------------------------------------#
    ###-------------------------------------------------------------###
    print(f'finished time {round(finish-start, 2)} s')
