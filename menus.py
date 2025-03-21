import utils
import functions


def main_menu():
    try:
        print("======== MENU ========")
        print("1 - Calculate totals")
        print("2 - Start tracking")
        print("3 - Stop tracking")
        print("4 - Quit the app")
        print("======================")
        choice = input("What would you like to do? ")
        if choice not in ["1", "2", "3", "4"]:
            raise utils.MenuOptionError
        return int(choice)
    except utils.MenuOptionError:
        utils.format_error("That is not a valid menu option, please try again!")


def calculate_totals_menu():
    utils.list_clients()
    client = input("Which client do you want to calculate totals for? ")
    if client in utils.return_clients():
        print("======== DATE RANGE ========")
        print("1 - Enter date range")
        print("2 - Check the last X days")
        print(f"3 - Retrieve all data for {client}")
        range_choice = input("Make your choice: ")
        if range_choice == "1":
            date_range_menu(client)
        elif range_choice == "2":
            last_x_days_menu(client)
        elif range_choice == "3":
            functions.display_all_totals(client)
        else:
            utils.format_error("That is not a valid option.")
    else:
        utils.format_error(f"{client} is not a client in your tracker")
    utils.back_to_main_menu()


def date_range_menu(client):
    print("Enter the date range in which you want to retrieve data from")
    user_input = input("Use the format [YYYY-MM-DD to YYYY-MM-DD]: ")
    try:
        split_dates = user_input.split(" to ")
        functions.display_range_totals(client, split_dates)
    except ValueError:
        utils.format_error("That's not a valid format")


def last_x_days_menu(client):
    try:
        user_input = int(input(f"Retrieve data on {client} from how many days ago? "))
        functions.display_x_days_totals(client, user_input)
    except ValueError:
        utils.format_error("That is not a valid number")


def start_tracking_menu():
    print("=========================")
    if utils.check_if_job_running():
        print("There is already a job being tracked. Let's stop it first.")
        print("Stopping job...")
        functions.stop_tracking()
        print("Previous job stopped")
        print("=========================")
    print("Who is the client?")
    utils.list_clients()
    client = input("Enter one of the above or a new client: ")
    description = input("Enter a short description: ")
    functions.start_tracking(client, description)
    print("=========================")
    utils.back_to_main_menu()


def stop_tracking_menu():
    if utils.check_if_job_running():
        print("=========================")
        functions.stop_tracking()
        print("=========================")
    else:
        utils.format_error("No job to stop tracking!")
    utils.back_to_main_menu()
