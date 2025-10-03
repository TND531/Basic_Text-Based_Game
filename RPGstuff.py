
# main menu stuff:


def main_menu_look():
    print("-" * 20, ">Main Menu<","1. Play", "2. How to Play", "3. Exit", "-" * 20, sep="\n")

def shutdown_animation(duration):
    import time
    start_time = time.time()
    dots = ['.', '..', '...']
    i = 0
    while time.time() - start_time < duration:
        print(f'\rShutting Down{dots[i % 3]}', end='')
        time.sleep(0.30)
        i += 1
    print()
    exit


# gameplay's stuff:

# animations:

def wait_animation(duration):
    import time
    start_time = time.time()
    dots = ['.', '..', '...']
    i = 0
    while time.time() - start_time < duration:
        print(f'\r{dots[i % 3]}', end='')
        time.sleep(0.25)
        i += 1
    print()


def sleep_animation(duration):
    import time
    start_time = time.time()
    dots = ['.', '..', '...']
    i = 0
    while time.time() - start_time < duration:
        print(f'\rSleeping{dots[i % 3]}', end='')
        time.sleep(0.5)
        i += 1
    print()


# other:


def print_inventory(inventory):
    # inventory's look code
    if inventory:
        items = ', '.join(f'{i+1}# {item}' for i, item in enumerate(inventory))
    else:
        items = 'Empty'
    # print inventory's items        
    print('-' * 20, '[Your Inventory]'.rjust(17), items, '-' * 20, sep='\n')
    

def print_energy_level(energy_level):
    if energy_level >= 20:
        print(f'Energy Level: {energy_level}')
    else:
        print(f'Energy Level: >{energy_level}< (running low)')
    print()


def print_options(options):
    print('>Your Move Options<\n')
    if options == 0:
        print('Sorry bro, but you can\t do anything rn (T- T)')
    else:
        for i, option in enumerate(options, start=1):
            print(f'{i}# {option}')


def users_option_input():
    # user's input: 
    while True:
        try:
            users_move = int(input('What\'s your choice?\n>'))
            if users_move in (1, 2, 3):
                return users_move 
            else:
                print('you can choose only the options avaible')
        except ValueError:
                print('you didn\'t print a number. ONLY numbers are acceptable')


# each stage:


def first_print_info(user_name):
    print(f'You are {user_name}.\nYou\'re in your bedroom and you\'re laying in your bed.')
    # show_room()


def outta_bed_info():
    print('You are in your bedroom. It has a big bed.\nOn the left side of the room there\'s (1) bedside cabinet and (2) a door which leads to the bathroom.\nOn the right side there\'s (1) a cabinet and (2) a door which leads to the closet.')


def bedside_cabinet_info(inventory):
    if 'Phone' not in inventory:
        phone_info = ' There\'s your phone on it.'
    else:
        phone_info = ''
    # print the information:
    print(f'You are right next to your bedside cabinet.{phone_info} The cabinet has also a small drawer.')


def take_the_phone(inventory):
    if 'Phone' in inventory:
        print('You already took the phone')
    else:
        inventory = inventory.append('Phone')
        print('You took the phone')


def go_cabinet_info():
    print('\nYou are right next to the cabinet.\nThere\'s a notebook on it. You cannot take the notebook.')


in_notebook = ''

def notebook_add():
    wait_animation(1)
    # user's input:
    added_stuff = input('What would you like to add?\n>')
    # adding to notebook:
    global in_notebook
    if in_notebook:
        in_notebook += '\n' + added_stuff
    else:
        in_notebook = added_stuff


def notebook_clear():
    global in_notebook
    in_notebook = ''

# in_notebook = ''


def cabinet_open_info():
        # print('')
        pass





































