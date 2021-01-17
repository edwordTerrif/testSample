import os
import pyautogui as pyg
import func_block_code as vega
from pynput import mouse, keyboard
import csv
import time
import random

tag = vega.target()
excep = vega.in_except()
in_battle = vega.designation_in_battle()
"""
time.sleep(2)
"""
# in_battle.dn_in_battle()
################################################################
# RECORD MOUSE CLICK
################################################################

#file = open(name , mode=mode)
# mode:
# new_file
# read_file
# over_write_file

# in game test section

############################################################################################
# macro tree sys #
# TODO first used macro ui and build function refrunce : #
##########################################----##############################################

"""
def space_on_press(key):
    if key == keyboard.Key.space:
        # start battle section
        pass
"""

"""
with keyboard.Listener(on_press=space_on_press) as listener:
    listener.join()
"""


class key_test():
    def __init__(self):
        self.mouse_listener = mouse.Listener(on_click=self.on_click)
        self.record_coods_list = []
        self.first_wait_time = 'perf_time'

    def on_press(self, key):
        if self.mouse_listener.running and key == keyboard.Key.space:
            self.mouse_listener.stop()
            print('stop listener', self.record_coods_list)
            return

        if not self.mouse_listener.running and key == keyboard.Key.space:
            print('start listener', self.mouse_listener.running)
            self.mouse_listener = mouse.Listener(on_click=self.on_click)
            self.first_wait_time = time.perf_counter()
            try:
                self.mouse_listener.start()
            except RuntimeError:
                print('Done')

        if key == keyboard.Key.esc:
            try:
                self.mouse.Listener.stop()
            except:
                print('listener already end')
            finally:
                return False

    ######////--                                                                              --\\\\######
    ##//                                                                                              \\##
    #/__                                                                                              __\#
    #                        shortcut key function ready for your key press                              #
    #                       if in the case localkey presed macro starting trigger                        #
    #/__                                                                                              __\#
    ##//                                                                                              \\##
    ######////--                                                                              --\\\\######

    def listener_shortcut_key(self):
        with keyboard.Listener(on_press=self.on_press) as key:
            try:
                key.join()
            except:
                print('Done')

    def on_click(self, x, y, btn, pressed):
        # left = btn = btn,left
        # right = btn = btn.right
        if pressed:
            self.start_time_loss = time.perf_counter()
            self.total_wait_time = self.start_time_loss - self.first_wait_time
            self.first_x = x
            self.first_y = y
            print(
                f"x:{x} y:{y} btn:{btn} pressed:{pressed} wait time:{self.start_time_loss ,self.first_wait_time, self.total_wait_time}")
        else:
            end_time_loss = time.perf_counter()
            self.first_wait_time = time.perf_counter()
            total_time_loss = end_time_loss - self.start_time_loss
            last_x = x
            last_y = y
            is_drag = self.first_x != last_x
            print(
                f'x:{x} y:{y} is drag:{is_drag} start sec:{total_time_loss}')
            self.record_coods_list.append(
                {
                    'click': {'btn_position': 'left' if btn == btn.left else 'right', 'in_battle_coord': {'x': self.first_x, 'y': self.first_y}, 'time loss': round(
                        total_time_loss, 2), 'wait time': round(self.total_wait_time, 2)},
                    'drag': {'btn_position': 'left' if btn == btn.left else 'right', 'in_battle_coord': {'x': last_x, 'y': last_y}, 'time loss': round(
                        total_time_loss, 2), 'wait time': round(self.total_wait_time, 2)} if is_drag else False
                }
            )


if __name__ == "__main__":
    # first record func excute time
    start = time.perf_counter()
    ###-------------------------------------------------------------###
    #-----------------------------------------------------------------#
    #                                                                 #
    #  execute key_test class function in the key_listener function   #
    #                                                                 #
    #-----------------------------------------------------------------#
    ###-------------------------------------------------------------###
    test = key_test()
    test.listener_shortcut_key()
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
""" 

for n in range(10):
    ts = round(random.uniform(a=881.1, b=900.1), 2)
    print(ts)
"""

################################################################
# COMMA SEPARATED VALUS SECTION / reter: IT USE IN EXCLE
# TODO: testing excle and coordnates position code save in text file
################################################################
