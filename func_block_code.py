import pyautogui as pyg
import cv2
import random
from pynput import mouse
import time


class target:
    def btn_click(self, img_taget):
        i = pyg.locateOnScreen(img_taget, confidence=.9)
        tag_cod = {
            'top_left': {
                'x': i[0],
                'y': i[1]
            },
            'bottom_right': {
                'x': i[0] + i[2],
                'y': i[1] + i[3]
            }
        }
        print(tag_cod)

        pyg.moveTo(x=random.uniform(tag_cod['top_left']['x'], tag_cod['bottom_right']['x']),
                   y=random.uniform(tag_cod['top_left']['y'], tag_cod['bottom_right']['y']))
        pyg.click()
        return

    def not_find_target(self):
        c = pyg.locateOnScreen('img_data/canNotFind.png', confidence=.9)
        if c != None:
            b = pyg.locateOnScreen(
                'img_data/canNotFind_btn.png', confidence=.9)
            btn_cod = {
                'top_left': {
                    'x': b[0],
                    'y': b[1]
                },
                'bottom_right': {
                    'x': b[0] + b[2],
                    'y': b[1] + b[3]
                }
            }
            pyg.moveTo(x=random.uniform(btn_cod['top_left']['x'], btn_cod['bottom_right']['x']),
                       y=random.uniform(btn_cod['top_left']['y'], btn_cod['bottom_right']['y']))
            pyg.click()
        else:
            return c
        print(c)


class record_in_battle:
    def __init__(self):
        self.none = None

    def in_battle(self):
        pass

    def timer(self):
        pass


class designation_in_battle:
    def __init__(self):
        self.get_missile = []

    def dn_in_battle(self):
        for c in self.get_missile:
            if c['drag'] == False:
                pyg.moveTo(x=random.uniform(c['click']['in_battle_coord']['x'], c['click']['in_battle_coord']['x'] + 0.3),
                           y=random.uniform(
                               c['click']['in_battle_coord']['y'], c['click']['in_battle_coord']['y'] + 0.3),
                           duration=random.uniform(c['click']['time loss'], c['click']['time loss'] + 0.1))
                pyg.mouseDown(button=c['click']['btn_position'], duration=random.uniform(
                    c['click']['time loss'], c['click']['time loss'] + 0.1))
                pyg.mouseUp(button=c['click']['btn_position'], duration=random.uniform(
                    c['click']['time loss'], c['click']['time loss'] + 0.1))
                time.sleep(random.uniform(
                    c['click']['wait time'], c['click']['wait time'] + 0.2))
            else:
                time.sleep(random.uniform(
                    c['drag']['wait time'], c['drag']['wait time'] + 0.2))
                pyg.moveTo(x=random.uniform(
                    c['click']['in_battle_coord']['x'], c['click']['in_battle_coord']['x'] + 0.3),
                    y=random.uniform(
                    c['click']['in_battle_coord']['y'], c['click']['in_battle_coord']['y'] + 0.3),
                    duration=random.uniform(
                    c['drag']['time loss'] - 0.1, c['drag']['time loss'])
                )
                pyg.dragTo(button=c['drag']['btn_position'],
                           x=random.uniform(
                               c['drag']['in_battle_coord']['x'], c['drag']['in_battle_coord']['x'] + 0.3),
                           y=random.uniform(
                               c['drag']['in_battle_coord']['y'], c['drag']['in_battle_coord']['y'] + 0.3),
                           duration=random.uniform(
                               c['drag']['time loss'] - 0.1, c['drag']['time loss'])
                           )


class in_except:
    def netwark_error(self):
        n = pyg.locateOnScreen('img_data/netwark_error.png', confidence=.9)
        if n != None:
            b = pyg.locateOnScreen(
                'img_data/netwark_error_btn.png', confidence=.9)
            btn_cod = {
                'top_left': {
                    'x': b[0],
                    'y': b[1]
                },
                'bottom_right': {
                    'x': b[0] + b[2],
                    'y': b[1] + b[3]
                }
            }
            pyg.moveTo(x=random.uniform(btn_cod['top_left']['x'], btn_cod['bottom_right']['x']),
                       y=random.uniform(btn_cod['top_left']['y'], btn_cod['bottom_right']['y']))
            pyg.click()
        else:
            return n
