import csv


def get_by_client(client):
    all_jobs = read_csv()
    client_jobs = list(filter(lambda row: row['client'] == client, all_jobs))
    return client_jobs


class MenuOptionError(Exception):
    """Raised when an invalid menu option is used"""
    pass


def format_error(error_message):
    print("\n#### ERROR ####")
    print(error_message)
    print("###############\n")


def list_clients():
    data = read_csv()
    print("Here is a list of clients that exist in the tracker")
    clients = {job['client'] for job in data}
    for client in clients:
        print(client)


def return_clients():
    data = read_csv()
    clients = {job['client'] for job in data}
    return clients


def read_csv():
    data = []
    with open('data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            data.append({
                'client': row['client'],
                'description': row['description'],
                'start_time': row['start_time'],
                'end_time': row['end_time'],
            })
    return data


def check_if_job_running():
    with open('data.csv', 'r') as csvfile:
        last_line = csvfile.readlines()[-1]
        last_character = last_line[-1]
        return last_character == ','


def back_to_main_menu():
    input("Press any key to return to main menu...")

