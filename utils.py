import csv
import datetime
from dateutil import relativedelta

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

def get_now_timestamp():
    now = datetime.datetime.now()
    format_string = "%I:%M%p %Y-%m-%d"
    return datetime.datetime.strftime(now, format_string)  # Return the formatted timestamp as a string

# Client Data Processing Function: Develop a versatile function that
# takes a client and a list of client job entries, then calculates and
# displays relevant data. Challenge yourself to use advanced Python
# features like list comprehension, filter(), and lambda functions to
# efficiently filter through client job entries based on specified date
# ranges. This function should provide valuable insights into client
# related data, making your Time Tracker app even more powerful and nformative.

def process_client_data(client, client_jobs, range_start_dt=None, range_end_dt=None):
    
    format_string_dt = "%I:%M%p %Y-%m-%d"
    # Filter client jobs based on the provided date range
    if range_start_dt and range_end_dt:
        filtered_jobs = list(filter(lambda job: range_start_dt <= datetime.datetime.strptime(job['end_time'], format_string_dt) <= range_end_dt, client_jobs))
    else:
        filtered_jobs = client_jobs

    # Calculate total time spent on filtered jobs using list comprehension
    total_time = sum(
        (datetime.datetime.strptime(job['end_time'], format_string_dt) - 
         datetime.datetime.strptime(job['start_time'], format_string_dt)).total_seconds() 
         for job in filtered_jobs
    )

    # Convert total time to hours and minutes
    total_hours = total_time // 3600
    total_minutes = (total_time % 3600) // 60

    # Display results
    for job in filtered_jobs:
        job_start_dt = datetime.datetime.strptime(job['start_time'], format_string_dt)
        job_end_dt = datetime.datetime.strptime(job['end_time'], format_string_dt)
        time_spent = relativedelta.relativedelta(job_end_dt, job_start_dt)
        
        print(f"{job['description']} - {time_spent.hours} hours {time_spent.minutes} minutes")
    
    print(f"Total for {client}: { int(total_hours) } hours { int(total_minutes) } minutes")

# Another alternative to convert total time to hours and minutes: 
# total_hours, total_minutes = divmod(total_time // 60, 60). 
# This is a pythonic way to convert total time in seconds to hours and minutes.
# The divmod() function takes two numbers and returns a tuple of their quotient and remainder.
# In this case, it divides total_time by 60 to get the total hours and minutes.