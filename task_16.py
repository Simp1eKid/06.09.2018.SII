#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_22():

    while (wall_is_above()==False):
        move_up(n=1)
    if (wall_is_on_the_left()==False):
        while (wall_is_on_the_left()==False):
            move_left(n=1)
    elif (wall_is_on_the_right()==False):
        while (wall_is_on_the_right()==False):
            move_right(n=1) 

            
    pass


if __name__ == '__main__':
    run_tasks()
