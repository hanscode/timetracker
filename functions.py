import csv
import utils
import datetime
from dateutil import relativedelta

def start_tracking(client, description):
    print(f"Start tracking {description} for {client}")

    # TODO: Grab the current time and store it as a string in start_time
    # in the format: HH:MM(AM/PM) YYYY-MM-DD
    # for example: 09:40AM 2023-08-11

    start_time = utils.get_now_timestamp()

    # Code to append a new job to the CSV
    with open('data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', lineterminator='')
        writer.writerow([client, description, start_time, ''])


def stop_tracking():
    print("Stopping tracking")

    # TODO: Grab the current time and store it as a string in end_time
    # in the format: HH:MM(AM/PM) YYYY-MM-DD
    # for example: 09:40AM 2023-08-11

    end_time = utils.get_now_timestamp()

    # Code to append a new job to the CSV
    with open('data.csv', 'a') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow([end_time])

# TODO: write a function that displays the total time spent on all jobs for a client
def display_all_totals(client):
    print(f"Calculating time spent on all jobs for {client}...")
    client_jobs = utils.get_by_client(client)

    # TODO: List out all the different jobs, and then a total time spent
    # For example, if the user chooses Emmerton:
    # Monthly Meeting - 1 hours 0 minutes
    # Onboarding replacement - 2 hours 0 minutes
    # Follow-up questions - 0 hours 28 minutes
    # TOTAL FOR EMMERTON: 3 hours 28 minutes

    total = relativedelta.relativedelta()

    for job in client_jobs:
        format_string = "%I:%M%p %Y-%m-%d"
        start_dt = datetime.datetime.strptime(job['start_time'], format_string)
        end_dt = datetime.datetime.strptime(job['end_time'], format_string)
        
        time_spent = relativedelta.relativedelta(end_dt, start_dt)
        
        print(f"{job['description']} - {time_spent.hours} hours {time_spent.minutes} minutes")
        
        total += time_spent
    
    print(f"TOTAL FOR {client}: {total.hours} hours {total.minutes} minutes")

    # references
    # print(client)
    # print(client_jobs)


# TODO: write a function that displays the total time spent on jobs for a client in a date range
def display_range_totals(client, dates_str_list):
    print(f"Calculating time spent on jobs for {client} in the specified range...")
    client_jobs = utils.get_by_client(client)

    # dates_str_list contains 2 date strings in the format YYYY-MM-DD
    # TODO: turn the two date strings in dates_str_list to datetime objects and store in range_start_dt and range_end_dt

    format_string = "%Y-%m-%d"
    try:
        range_start_dt = datetime.datetime.strptime(dates_str_list[0], format_string)
        range_end_dt = datetime.datetime.strptime(dates_str_list[1], format_string).replace(hour=23, minute=59, second=59)
    except ValueError:
        # Use format_error(error_message) to display the error message
        utils.format_error(f"Oops! Invalid date format: '{dates_str_list}'. Expected format is YYYY-MM-DD.")
        return # Exit the function if the date format is invalid

    # TODO: filter client_jobs to only include those within the start and end datetimes

    total = relativedelta.relativedelta()

    for job in client_jobs:
        format_string_dt = "%I:%M%p %Y-%m-%d"
        job_end_dt = datetime.datetime.strptime(job['end_time'], format_string_dt)

        if range_end_dt > job_end_dt > range_start_dt:
            job_start_dt = datetime.datetime.strptime(job['start_time'], format_string_dt)
            time_spent = relativedelta.relativedelta(job_end_dt, job_start_dt)

            #print(time_spent)
            # TODO: List out all the different jobs, and then a total time spent - just like display_all_totals
            print(f"{job['description']} - {time_spent.hours} hours {time_spent.minutes} minutes")
            total += time_spent
        
    print(f"Total for {client}: {total.hours} hours {total.minutes} minutes")


# TODO: write a function that displays the total time spent on jobs for a client in the last X days
def display_x_days_totals(client, days):
    print(f"Calculating time spent on jobs for {client} in the last {days} days...")
    client_jobs = utils.get_by_client(client)

    # TODO: determine the start and end datetimes for this range
    go_back_days = datetime.timedelta(days=days)
    range_start_dt = datetime.datetime.now() - go_back_days
    range_end_dt = datetime.datetime.now()

    # TODO: filter and display client_jobs to only include those with the start and end datetimes
    total = relativedelta.relativedelta()

    for job in client_jobs:
        format_string = "%I:%M%p %Y-%m-%d"
        job_end_dt = datetime.datetime.strptime(job['end_time'], format_string)

        if range_end_dt > job_end_dt > range_start_dt:
            job_start_dt = datetime.datetime.strptime(job['start_time'], format_string)
            time_spent = relativedelta.relativedelta(job_end_dt, job_start_dt)

            #print(time_spent)
            print(f"{job['description']} - {time_spent.hours} hours {time_spent.minutes} minutes")
            total += time_spent
    
    print(f"Total for {client}: {total.hours} hours {total.minutes} minutes")

