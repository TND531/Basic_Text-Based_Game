
from RPGstuffstages import (
    main_menu,
    m_m_play,
    m_m_how_to_play,
    m_m_exit
    )

def main():
    main_menu()
    main_menu_option = input(">")
    match main_menu_option:
        case "1":
            m_m_play(main_menu_option)
        case "2":
            m_m_how_to_play()
        case "3":
            m_m_exit()

main()



