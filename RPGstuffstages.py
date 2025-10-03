# TO DO: 1) Add the Energy/Food level. 
#        2) ...
#        3) ...
#        4) ...
# FIX:   1) ...

import RPGstuff

# MAIN MENU:

def main_menu():
    while True:
        print(RPGstuff.main_menu_look())
        break

# its options:

def m_m_play(main_menu_option):
    start_playing(main_menu_option)

def m_m_how_to_play():
    ...

def m_m_exit():
    RPGstuff.shutdown_animation(3)

# THE GAME

def start_playing(main_menu_option):
    RPGstuff.wait_animation(1)
    # 1st STAGE:
    print(f'You have chosen option \'{main_menu_option}\' (Play).')
    user_name = user_name_ask()
    # to the first_in_bed()
    energy_level = 100
    RPGstuff.wait_animation(1)
    first_in_bed(user_name, energy_level)
    
def user_name_ask():
    return input('What\'s your name?\n>')

# the game:

def first_in_bed(user_name, energy_level):
    while True:
        # info about the situation:
        RPGstuff.first_print_info(user_name)
        # inventory:
        inventory = []
        RPGstuff.print_inventory(inventory)
        # energy level:
        RPGstuff.print_energy_level(energy_level)
        # options:
        options = ['Get out of the bed', 'Sleep', 'nothing for opt.3 yet']
        # user's move options avaible:
        RPGstuff.print_options(options)
        # user's move input:
        users_option = RPGstuff.users_option_input()
        # the execution of user's move option:
        match users_option:
            case 1:
                print(f'You have chosen option \'{users_option}\'.')
                outta_bed(user_name, inventory, energy_level)
                break
            case 2:
                print(f'You have chosen option \'{users_option}\'.')
                RPGstuff.sleep_animation(5)
                first_in_bed(user_name, energy_level)
                break 
            case 3:
                print('nothing for 3 yet')
                break 

def outta_bed(user_name, inventory, energy_level):
    while True:
        RPGstuff.wait_animation(1)
        # information:
        RPGstuff.outta_bed_info()
        # inventory: 
        RPGstuff.print_inventory(inventory)
        options = ['Go to the left side.', 'Go to the right side.', 'Go to bed.']
        # user's move options avaible:
        RPGstuff.print_options(options)
        # user's move input:
        users_option = RPGstuff.users_option_input()
        # the execution of user's move option:
        match users_option:
            case 1:
                print(f'You have chosen option \'{users_option}\'.')
                go_left(user_name, inventory, energy_level)
                break
            case 2:
                print(f'You have chosen option \'{users_option}\'.')
                go_right(user_name, inventory, energy_level)
                break 
            case 3:
                # go to bed:
                print(f'You have chosen option \'{users_option}\'.')
                RPGstuff.wait_animation(1)
                first_in_bed(user_name, energy_level)
                break 

def go_left(user_name, inventory, energy_level):
    while True:
        RPGstuff.wait_animation(1)
        # information:
        # go_left_info()
        # 
        RPGstuff.print_inventory(inventory)
        options = ['Go to the bedside cabinet.', 'Go through the door which leads to the bathroom.', 'Go back.']
        # user's move options avaible:
        RPGstuff.print_options(options)
        # user's move input:
        users_option = RPGstuff.users_option_input()
        # the execution of user's move option:
        match users_option:
            case 1:
                print(f'You have chosen option \'{users_option}\'.')
                bedside_cabinet(user_name, inventory, energy_level)
                break
            case 2:
                print('nothing for 2 yet')
                break 
            case 3:
                # going back:
                print(f'You have chosen option \'{users_option}\'.')
                outta_bed(user_name, inventory, energy_level)
                break 

def bedside_cabinet(user_name, inventory):
    while True:
        RPGstuff.wait_animation(1)
        # information:
        RPGstuff.bedside_cabinet_info(inventory)
        # inventory
        RPGstuff.print_inventory(inventory)
        # user's options
        if 'Phone' not in inventory:
            take_phone_option = 'Take the phone.'
        else:
            take_phone_option = '*Phone already tooken*'
        options = [take_phone_option, 'Open the drawer.', 'Go back.']
        # user's move options avaible:
        RPGstuff.print_options(options)
        # user's move input:
        users_option = RPGstuff.users_option_input()
        # the execution of user's move option:
        match users_option:
            case 1:
                print(f'You have chosen option \'{users_option}\'.')
                RPGstuff.take_the_phone(inventory)
                continue
            case 2:
                print('nothing for 2 yet')
                break 
            case 3:
                # going back:
                print(f'You have chosen option \'{users_option}\'.')
                go_left(user_name, inventory)
                break 


def go_right(user_name, inventory):
    while True:
        RPGstuff.wait_animation(1)
        # information:
        # go_right_info()
        # 
        RPGstuff.print_inventory(inventory)
        options = ['Go to the cabinet.', 'Go through the door which leads to the closet.', 'Go back.']
        # user's move options avaible:
        RPGstuff.print_options(options)
        # user's move input:
        users_option = RPGstuff.users_option_input()
        # the execution of user's move option:
        match users_option:
            case 1:
                print(f'You have chosen option \'{users_option}\'.')
                go_cabinet(user_name, inventory)
                break
            case 2:
                print('nothing for 2 yet')
                break 
            case 3:
                # going back:
                print(f'You have chosen option \'{users_option}\'.')
                outta_bed(user_name, inventory)
                break 

def go_cabinet(user_name, inventory):
    while True:
        RPGstuff.wait_animation(1)
        # information:
        RPGstuff.go_cabinet_info()
        # 
        RPGstuff.print_inventory(inventory)
        options = ['Open the notebook.', 'Open the cabinet.', 'Go back.']
        # user's move options avaible:
        RPGstuff.print_options(options)
        # user's move input:
        users_option = RPGstuff.users_option_input()
        # the execution of user's move option:
        match users_option:
            case 1:
                print(f'You have chosen option \'{users_option}\'.')
                open_notebook(user_name, inventory)
                break
            case 2:
                print('nothing for 2 yet')
                cabinet_open(user_name, inventory)
                break 
            case 3:
                # going back:
                print(f'You have chosen option \'{users_option}\'.')
                go_right(user_name, inventory)
                break 


def open_notebook(user_name, inventory):
    while True:
        RPGstuff.wait_animation(1)
        # the look of the notebook:
        print('-' * 20, RPGstuff.in_notebook, '-' * 20, sep='\n')
        # options:
        options = ['Add.', 'Clear all.', 'Go back.']
        # user's move options avaible:
        RPGstuff.print_options(options)
        # user's move input:
        users_option = RPGstuff.users_option_input()
        # the execution of user's move option:
        match users_option:
            case 1:
                print(f'You have chosen option \'{users_option}\'.')
                RPGstuff.notebook_add()
                open_notebook(user_name, inventory)
            case 2:
                print(f'You have chosen option \'{users_option}\'.')
                RPGstuff.notebook_clear()
                open_notebook(user_name, inventory)
            case 3:
                # going back:
                print(f'You have chosen option \'{users_option}\'.')
                go_cabinet(user_name, inventory)
                break 


def cabinet_open(user_name, inventory):
    while True: 
        RPGstuff.wait_animation(1)
        ...










































































