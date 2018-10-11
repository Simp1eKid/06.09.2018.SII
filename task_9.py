#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_2():
    while (wall_is_beneath() and wall_is_on_the_right()==False):
        if (wall_is_above()==False) and (wall_is_on_the_right()==False):
            fill_cell()
        move_right(n=1)
        if (wall_is_on_the_right and wall_is_above()==False):
            fill_cell()
    pass


if __name__ == '__main__':
    run_tasks()
