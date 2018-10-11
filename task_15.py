#!/usr/bin/python3

from pyrob.api import *
 
@task
def task_8_21():
    if wall_is_above() and wall_is_on_the_left():
        while wall_is_on_the_right()==False:
            move_right(n=1)
        while wall_is_beneath()==False:
            move_down(n=1)
    elif wall_is_on_the_right() and wall_is_above():
        while wall_is_beneath()==False:
            move_down(n=1)
        while wall_is_on_the_left()==False:
            move_left(n=1)
    elif  wall_is_beneath() and wall_is_on_the_right():
        while wall_is_on_the_left()==False:
            move_left(n=1)
        while wall_is_above()==False:
            move_up(n=1)
    elif  wall_is_beneath() and wall_is_on_the_left():
        while wall_is_above()==False:
            move_up(n=1)
        while wall_is_on_the_right()==False:
            move_right(n=1)
    pass


if __name__ == '__main__':
    run_tasks()
