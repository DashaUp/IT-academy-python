from cat import *
import random


coco = Cat('Coco')
for day in range(1, 365):
    if coco.is_alive() == False:
        break
    coco.live(day)
