import menus

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("WELCOME TO THE TIME TRACKING APP")
    menu_choice = 0
    while menu_choice != 4:
        menu_choice = menus.main_menu()
        if menu_choice == 1:
            menus.calculate_totals_menu()
        if menu_choice == 2:
            menus.start_tracking_menu()
        if menu_choice == 3:
            menus.stop_tracking_menu()
    print("Have a great day!")

