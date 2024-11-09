
from human import *
day = 1

vasia = Human()
vasia.get_car()
vasia.get_home()
vasia.get_job()
while vasia.alive:
    vasia.live(day)
    day += 1
