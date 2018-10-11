#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_3():
    if (wall_is_above()==False) and (wall_is_beneath()==True) and (wall_is_on_the_left()==True) and (wall_is_on_the_right()==True):
       move_up(1)
    if (wall_is_above()==True) and (wall_is_beneath()==False) and (wall_is_on_the_left()==True) and (wall_is_on_the_right()==True):
       move_down(1)
    if (wall_is_above()==True) and (wall_is_beneath()==True) and (wall_is_on_the_left()==False) and (wall_is_on_the_right()==True):
       move_left(1)
    if (wall_is_above()==True) and (wall_is_beneath()==True) and (wall_is_on_the_left()==True) and (wall_is_on_the_right()==False):
       move_right(1)

    pass


if __name__ == '__main__':
    run_tasks()
